# CryptoSpark
Big Data Analytics Uncovering Insights from Binance Historical Market Data

dataset: https://www.kaggle.com/datasets/jorijnsmit/binance-full-history

File/Object storage: AWS S3
Big Data Compute: Spark(python)
Vizualization: Apache Zeppelin 

## Syncing the Binance Full History Dataset to S3

Before running any Spark analytics, we upload the raw Parquet files directly from our local archive folder into Amazon S3:

```bash
# Sync only new or changed files from local → S3
aws s3 sync "C:\Path\DATA-228\project\archive" s3://cryptospark-dataset/archive/
````

* **Local path**: the directory containing all `.parquet` files of minute-level candlesticks
* **S3 URI**: `s3://cryptospark-dataset/archive/` in the `cryptospark-dataset` bucket
* The `sync` command compares source and destination and uploads **only** missing or updated files, saving bandwidth and time.

## Prerequisites

* **AWS Account** with an S3 bucket named `cryptospark-dataset`.
* **IAM User** (e.g., `Niranjan`) in the `crypto-analysts` group with full S3 access to `s3://cryptospark-dataset/*`.
* **WSL (Ubuntu)** or Linux/macOS environment.
* **VS Code** (or any code editor) with Python 3 installed.

**Install system dependencies** (Java, Python, pip) in WSL:

   ```bash
   sudo apt update
   sudo apt install -y default-jdk python3 python3-pip
   ```
**Install AWS CLI**:

   ```bash
   sudo pip3 install --break-system-packages awscli
   ```
**Install Python libraries** for data wrangling:

   ```bash
   sudo pip3 install --break-system-packages awswrangler pandas pyarrow
   ```

## AWS CLI Configuration

Configure your IAM user credentials:

```bash
aws configure
# Enter your Access Key ID, Secret Access Key, default region (us-east-1), and default output (json)
```

Verify access:

```bash
aws s3 ls s3://cryptospark-dataset/archive/
```
