# Metabase + Spark SQL Integration

This README walks through the steps to expose your local Spark dataset via the Spark Thrift Server and connect it as a database in Metabase for interactive visualization.

---

## 1. Prerequisites

* **Local Spark installation** (e.g., Spark 3.5.5 with Hive support)
* **Metabase** Docker container or binary
* **Data folder** (`archive/`)
* Network access between Metabase and your host’s Spark Thrift port (default 10000)

---

## 2. Prepare your Spark Catalog

1. **Create a Spark SQL database** and register the raw Parquet files:

   ```bash
   $SPARK_HOME/bin/spark-sql --master local[3] <<SQL
   CREATE DATABASE IF NOT EXISTS crypto;
   USE crypto;
   DROP TABLE IF EXISTS archive;
   CREATE EXTERNAL TABLE archive
     USING PARQUET
     LOCATION '/archive';
   SQL
   ```

2. **Verify tables** via `spark-sql`:

   ```bash
   $SPARK_HOME/bin/spark-sql --master local[3] \
     -e "SHOW TABLES IN crypto;"
   # Should list `archive` table
   ```

---

## 3. Start the Spark Thrift Server

Launch HiveThriftServer2 on `localhost:10000`:

```bash
$SPARK_HOME/sbin/start-thriftserver.sh \
  --master local[*] \
  --conf spark.sql.warehouse.dir=/tmp/warehouse \
  --conf spark.sql.catalogImplementation=hive \
  --conf spark.sql.hive.metastore.jars=builtin
```

Check it's running:

```bash
$ netstat -tulpn | grep 10000
# tcp6 ... LISTEN ... java
```

---

## 4. Connect Metabase to Spark

1. **Run Metabase** (host network mode):

   ```bash
   ```

docker run -d --name metabase --network host metabase/metabase

```
2. **Open Metabase** at `http://localhost:3000` and go through initial setup.
3. **Add a new database**:
   - **Database type**: Spark SQL
   - **Host**: `localhost`
   - **Port**: `10000`
   - **Database name**: `crypto`
   - **Username / Password**: leave blank (no auth)

If you see "Couldn't connect", ensure:
- Thrift server is listening on `localhost:10000`
- Metabase can reach `localhost` (use `--network host`)

---

## 5. Explore Your Data

1. In Metabase, go to **Browse → Databases → Crypto**.
2. Select the **archive** table to view the raw data.
3. Use **Summarize**, **Filter**, or **SQL Editor** to build queries:
   - **Daily metrics**: average, min/max, sum of `volume`
   - **Moving averages**: window functions over `close` price
   - **Volatility**: `(high - low)/open`

4. **Save questions** and build **Dashboards**.

---

## 6. Troubleshooting

- **Connection refused**: confirm Thrift server is up and listening.
- **UnknownHostException**: ensure Metabase container’s host settings point to your Spark host.
- **Permission errors**: start Thrift server with user owning the warehouse directory.

---

## 7. Next Steps

- Automate Spark Thrift Server startup on login or as a service.
- Extend your Spark SQL catalog with pre-processed tables (e.g., daily returns).
- Secure the connection with authentication, SSL, or SSH tunneling.
- Share dashboards and embed visualizations in external apps.

---

```
