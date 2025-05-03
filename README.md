# CryptoSpark
Big Data Analytics Uncovering Insights from Binance Historical Market Data

dataset: https://www.kaggle.com/datasets/jorijnsmit/binance-full-history

File/Object storage: AWS S3
Big Data Compute: Spark(python)
Vizualization: Apache Zeppelin 

## Syncing the Binance Full History Dataset to S3

Before running any Spark analytics, we upload the raw Parquet files directly from our local archive folder into Amazon S3 using the AWS CLI:

```bash
# Sync only new or changed files from local → S3
aws s3 sync \
  "C:/Users/niran/OneDrive/Documents/DATA-228/project/archive" \
  s3://cryptospark-dataset/archive/
````

* **Local path**: the directory containing all `.parquet` files of minute-level candlesticks
* **S3 URI**: `s3://cryptospark-dataset/archive/` in the `cryptospark-dataset` bucket
* The `sync` command compares source and destination and uploads **only** missing or updated files, saving bandwidth and time.
