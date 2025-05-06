import awswrangler as wr

# Read just one Parquet file to test connectivity
df = wr.s3.read_parquet(
    path="s3://cryptospark-dataset/archive/ADA-BTC.parquet",
    dataset=False  # single file
)
print("Read sample rows:", len(df))
print(df.head())
