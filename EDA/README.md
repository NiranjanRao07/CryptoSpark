# Binance Market Data - Exploratory Data Analysis (EDA), Preprocessing & Feature Engineering

This Apache Zeppelin notebook (`Binance-EDA.zpln`) performs scalable exploratory data analysis (EDA) on Binance crypto trading data using PySpark.

---

## 📈 What’s in the Notebook?

The notebook covers:

### 📦 Data Loading
- Load from S3 or local disk (Parquet format)
- Schema inspection and first few rows

### 🧪 Basic EDA
- Descriptive statistics (`open`, `high`, `low`, `close`, `volume`)
- Time range check

### 📅 Daily Aggregation
- First open, last close, max high, min low
- Average closing price and total daily volume
- **Visualization**: Display daily OHLC summary using `z.show()`

### 📊 Moving Average
- 7-day moving average window for smoothing trends
- **Visualization**: Display moving average result using `z.show()`

### 🔍 Buy Pressure Ratio
- Ratio of taker buy quote volume to total quote asset volume
- Indicates market pressure
- **Visualization**: Display daily buy pressure ratio using `z.show()`

### 🌩️ Volatility (Candle Range)
- High minus low, averaged per day
- **Visualization**: Display volatility pattern using `z.show()`

### ⚠️ Outlier Detection
- Detect candles with the largest high-low range
- **Visualization**: Show outliers using `z.show()`

### 📈 Daily Trade Counts
- Aggregated number of trades per day
- **Visualization**: Display daily trades using `z.show()`

### 🕒 Hourly Patterns
- Average closing price and volume by hour of day
- **Visualization**: Display hourly trading patterns using `z.show()`

---

## 🧠 Tech Stack

- **Apache Zeppelin**: Notebook interface and visualizations
- **PySpark**: Distributed processing of large-scale data
- **Spark SQL**: Structured querying for efficient group-by, filters, and aggregation

---

## 📂 How to Use

1. Open Apache Zeppelin
2. Click **Import Note**
3. Upload `Binance-EDA.zpln`
4. Run each paragraph to generate charts and tables

---

## 📝 Notes

- `.zpln` files are Zeppelin-specific and must be viewed inside Zeppelin
- Charts (from `z.show()`) will not be visible on GitHub, only inside Zeppelin UI
- Data format expected: Parquet, with fields like `open_time`, `close`, `high`, `low`, `volume`, etc.

---

## 🔄 Data Cleaning
- Dropped unnecessary columns: `quote_asset_volume`, `number_of_trades`, etc.
- Removed rows with missing values in critical fields: `open`, `high`, `low`, `close`, `volume`, `date`.

## 🧮 Feature Engineering
- **Daily Return**: `(close - open) / open` — Measures daily price change.
- **Volatility**: `(high - low) / open` — Captures intraday price spread.
- **Moving Averages**: 7-day (`ma_7`) and 30-day (`ma_30`) moving averages on close.
- **Cumulative Return** *(optional)*: Running product of log returns per symbol.
- **Buy Pressure Ratio** *(if available)*: Ratio of taker buy volume to total quote volume.

## ⚙️ Partitioning and Optimization
- Repartitioned data by `symbol` to optimize Spark transformations.
- Used `.cache()` to reduce recomputation in multi-stage pipelines.

## 📤 Export
- Final DataFrame written to S3 in partitioned Parquet format: `s3a://cryptospark-dataset/processed-data/`
- Ready for downstream ML tasks like return prediction, volatility clustering, or anomaly detection.


