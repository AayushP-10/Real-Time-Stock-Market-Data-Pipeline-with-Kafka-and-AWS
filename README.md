# Real-Time-Stock-Market-Data-Pipeline-with-Kafka-and-AWS

# Introduction

This project showcases an End-to-End Data Engineering Pipeline for analyzing real-time stock market data using cutting-edge technologies like Apache Kafka and Amazon Web Services (AWS). The system is designed to simulate stock market data, process it in real-time, and store it for efficient querying and analysis.

The architecture integrates multiple tools and services, ensuring a seamless and scalable pipeline for real-time data ingestion, storage, and processing.

# Architecture

![image](https://github.com/user-attachments/assets/d165bc2a-cde6-42bf-a568-2449412d5555)

High-level overview of the architecture:

1. Data Producer: Simulates stock market data and streams it to Kafka using Python and the Boto3 SDK.
2. Apache Kafka: Handles distributed messaging, streaming stock market data from producers to consumers.
3. Data Consumer: Consumes Kafka streams and writes the data to Amazon S3.
4. Amazon S3: Scalable cloud storage for raw and processed stock market data.
5. AWS Glue Crawler & Catalog: Automatically discovers and catalogs the data schema.
6. Amazon Athena: Enables querying of the stock market data directly from S3 using SQL.

# Technologies used:

This project leverages the following technologies and tools:

Programming Language
1. Python
Amazon Web Services (AWS)
1. S3 (Simple Storage Service): For storing raw and processed data.
2. Glue Crawler: To automatically detect the data schema in S3.
3. Glue Catalog: To maintain the metadata of the datasets.
4. Athena: For querying the stock market data using SQL.
5. EC2 (Elastic Compute Cloud): To host and run Kafka.
Data Streaming and Processing
1. Apache Kafka: For real-time streaming and processing of stock market data.

# Features
1. Real-time stock market data simulation and ingestion.
2. Distributed data streaming with Apache Kafka.
3. Scalable storage of data in AWS S3.
4. Schema discovery and metadata cataloging using AWS Glue.
5. SQL-based querying and analysis of data using AWS Athena.

# How It Works
1. Producer: Python script generates simulated stock market data and streams it to Kafka.
2. Kafka Cluster: Acts as a broker to handle streaming messages.
3. Consumer: A Python script consumes the Kafka messages and uploads them to an S3 bucket.
4. AWS Glue: Discovers the data schema and catalogs it.
5. AWS Athena: Allows SQL-based analysis of the stock market data stored in S3.
