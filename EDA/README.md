# Binance Market Data - Exploratory Data Analysis (EDA), Preprocessing & Feature Engineering

This notebook performs an in-depth EDA on the Binance full history dataset (~35GB of 1-minute OHLCV data across 1000+ trading pairs from 2017–2022). The goal was to reduce data complexity, identify a representative symbol, and analyze its market behavior.

🧹 Step 1: Data Reduction
Read raw Parquet files into a Spark DataFrame

Aggregated minute-level data to daily-level using groupBy(symbol, date)

Calculated daily metrics:

avg(open), avg(close)

max(high), min(low)

sum(volume), sum(number_of_trades)

sum(taker_buy_base_asset_volume)

Cached the daily DataFrame for efficient re-use

🔍 Step 2: Symbol Selection
Computed average daily volume and price for each symbol

Applied filters:

Volume > 1,000,000

Price > $10

Selected LUNA-USDT for analysis due to its high liquidity and trading activity

📈 Topic A: Price Trend & Volatility
Analyzed daily average close with 7-day and 30-day moving averages

Calculated volatility as (high - low) / open

Identified a boom-bust cycle with a sharp crash in mid-2022

📉 Topic B: Volume vs. Price Return
Computed daily price return

Calculated correlation between volume and return (≈ -0.566)

Found that high volume often aligned with price drops, suggesting sell-side pressure

🟢 Topic C: Taker Buy Ratio & Bullish Signals
Calculated taker buy ratio and applied 7-day moving average

Defined bullish signals as high ratio (> 0.6) with positive return

No days met both criteria, indicating buyer dominance did not lead to price gains

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


