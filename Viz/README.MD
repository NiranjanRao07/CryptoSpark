# CryptoSpark Demo

A minimal end-to-end example showing how to:

1. **Process** large parquet trade files with PySpark  
2. **Engineer** features (daily return, volatility, moving averages)  
3. **Train** a logistic-regression model  
4. **Serve** predictions via a Flask API  
5. **Interact** with a Streamlit dashboard

---

## 📦 Repository Structure

```

.
├── data/                      # Raw & processed parquet files
├── models/                    # Saved Spark ML `PipelineModel`
├── api.py                     # Flask app serving `/predict` endpoint
├── app.py                     # Streamlit dashboard
├── requirements.txt           # Python dependencies
└── README.md                  # This file

````

---

## 🚀 Quick Start

### 1. Install dependencies

Create & activate a virtual environment, then:

```bash
pip install --break-system-packages -r requirements.txt
````

### 2. Preprocess & train (optional)

If you need to regenerate features or retrain:

```bash
# Launch PySpark shell or run your notebook/script:
python preprocess_and_train.py
# → produces `data/processed-data/` and `models/logistic.pipeline`
```

### 3. Run the Flask API

```bash
export FLASK_APP=api.py
python -m flask run
```

By default you’ll have a server at `http://127.0.0.1:5000/predict`.

### 4. Launch the Streamlit UI

```bash
streamlit run app.py
```

Interactively explore your model’s predictions in the browser.

---

## 🔧 Configuration

* **Spark**: configured in `api.py` / `app.py` via `SparkSession.builder`.
* **Model**: loaded with `PipelineModel.load("models/logistic.pipeline")`.
* **Flask**: simple JSON POST `/predict` → `{ features: […] }`.
* **Streamlit**: reads user inputs, calls Flask API, displays results.

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch
3. Commit & push your changes
4. Open a pull request

---
