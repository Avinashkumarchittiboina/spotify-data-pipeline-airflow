from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime, timedelta

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotify_airflow_pipeline
import boto3
from io import StringIO
import pandas as pd


default_args = {
    "owner": "avinash",
    "depends_on_past": False,
    "start_date": datetime(2024,11,2)
}

def _fetch_spotify_data(**kwargs):
    client_id = Variable.get("spotify_client_id")
    client_secret = Variable.get("spotify_client_secret")

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    #playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
    playlist_link = "https://open.spotify.com/playlist/5ABHKGoOzxkaa28ttQV9sE"
    #playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    playlist_URI = playlist_link.split("/")[-1]
    
    spotify_data = sp.playlist_tracks(playlist_URI)  

    filename ="spotify_raw_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".json"

    kwargs['ti'].xcom_push(key="spotify_filename", value=filename)
    kwargs['ti'].xcom_push(key="spotify_data", value=json.dumps(spotify_data))


def _read_data_from_s3(**kwargs):
    s3_hook = S3Hook(aws_conn_id = "aws_conn")
    bucket_name = "spotify-etl-project-avinash74"
    prefix= "raw_data/to_processed/"

    keys = s3_hook.list_keys(bucket_name=bucket_name, prefix = prefix)

    spotify_data = []
    for key in keys:
        if key.endswith(".json"):
            data = s3_hook.read_key(key, bucket_name)
            spotify_data.append(json.loads(data))

    kwargs['ti'].xcom_push(key="spotify_data" , value = spotify_data)

dag = DAG(
    dag_id = "sporify_etl_dag_airflow",
    default_args=default_args,
    description= "ETL Process for Spotify Data",
    schedule_interval=timedelta(days=1),
    catchup=False
)


fetch_data = PythonOperator(
    task_id =  "fetch_spotify_data",
    python_callable = _fetch_spotify_data,
    dag = dag,
)

store_raw_to_s3 = S3CreateObjectOperator(
    task_id = "Upload_raw_to_s3",
    aws_conn_id = "aws_conn",
    s3_bucket = "spotify-etl-project-avinash74",
    s3_key = "raw_data/to_processed/{{task_instance.xcom_pull(task_ids='fetch_spotify_data',key='spotify_filename')}}",
    data = "{{task_instance.xcom_pull(task_ids='fetch_spotify_data',key = 'spotify_data')}}",
    replace = True,
    dag = dag
)

read_data_from_s3 = PythonOperator(
    task_id = "read_data_from_s3",
    python_callable = _read_data_from_s3,
    provide_context = True,
    dag = dag,

)

fetch_data >> store_raw_to_s3 >> read_data_from_s3
