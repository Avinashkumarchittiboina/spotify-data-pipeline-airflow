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

# Prerequisites :

1.AWS Account
2.Spotify API credentials
3.Docker Installtion
4.Python latest version

