import os
import time
import awswrangler as wr

# Optional: ensure region is set (if CLI isn't picked up)
os.environ["AWS_REGION"] = "us-east-1"

print("🚀 Starting read from S3...")

start_time = time.time()  # Start the timer

try:
    df = wr.s3.read_parquet(
        path="s3://cryptospark-dataset/archive/ADA-BTC.parquet",
        dataset=False
    )
    end_time = time.time()  # End the timer

    duration = end_time - start_time
    print(f"✅ Read sample rows: {len(df)}")
    print(df.head())
    print(f"⏱️ Time taken: {duration:.2f} seconds")

except Exception as e:
    print("❌ Error occurred:", e)

