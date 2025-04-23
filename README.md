# Spotify data pipelline using Airflow,AWS,Spark

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Spotify data. The pipeline leverages a combination of tools and services including Apache Airflow, Docker, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena,Snowflake and Amazon Redshift.

# Overview

The pipeline is designed to:
1.Extract data from Spotify using its API.
2.Build Airflow on Docker.
3.Extract using AWS Lambda.
4.Store data into AWS S3.
5.Transform using AWS Glue.
6.Store the transformed data into S3.
7.Load the data into Snowflake using snowpiple.

All the above tasks are orchestrated in Airflow.This project can be executed in many ways.

# Architecture
**Scenario 1**
Using Airflow, all the tasks are orchestrated from Extacting to data analyzing.

![Airflow data pipeline scenario 1](https://github.com/user-attachments/assets/794b96da-2353-41f4-8a91-6b2387b28aa6)

**Scenario 2**
Use Airflow only at Transform layer. Remaining layers are taken care by AWS Services.

![Airflow data pipeline scenario 2](https://github.com/user-attachments/assets/b609c88c-9c54-4d06-930e-d3fff9aa51dd)

**Scenario 3**
![Airflow data pipeline scenario 3](https://github.com/user-attachments/assets/a39aa9e0-7558-4caa-9ce5-0e38a02912a5)

**Using python**
![image](https://github.com/user-attachments/assets/8d1d3b3b-d2dd-4922-bb37-ee71223c0d61)

**Airflow,Pyspark,EMR,Snowflake**

![image](https://github.com/user-attachments/assets/2853e0ee-89e4-4fab-a7e5-5849c565232d)

**Complete flow mamaged within AWS**

![image](https://github.com/user-attachments/assets/aca31ebc-074f-4915-93b0-b0df5eff5eb3)

**Project 2**

![image](https://github.com/user-attachments/assets/56ee164e-e305-462c-81ec-83cf9e8c669f)

**Project 3**

![image](https://github.com/user-attachments/assets/03b3ddce-2d88-426d-9c22-b36e8a38d223)

**Project 4**

![image](https://github.com/user-attachments/assets/172ca7fb-ca9e-43b8-aa12-58419d34ef3c)

**AWS , Azure,GCP**

![image](https://github.com/user-attachments/assets/3d0b2a2a-f2b8-4a03-9889-f52847fe6d74)

**AWS , SNOWFLAKE**

![image](https://github.com/user-attachments/assets/ea9f3808-089d-403e-a87b-1c7c0556d189)

**AWS glude to snowflake (bypassing to S3) **

![image](https://github.com/user-attachments/assets/70bc6a80-be4d-4322-b851-72cca479b880)


# Prerequisites :

1.AWS Account
2.Spotify API credentials
3.Docker Installtion
4.Python latest version

