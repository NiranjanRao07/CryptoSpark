from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml import PipelineModel

import os
os.environ["PYSPARK_PYTHON"] = "/home/niranjanrao07/crypto-spark/CryptoSpark/venv/bin/python3"

# Start Spark
spark = SparkSession.builder.appName("ModelAPI").getOrCreate()

# Load model
model = PipelineModel.load("logisticRegression_model")

# Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    feature_list = data['features']  # List of 14 numeric values

    # Create DataFrame with features
    columns = ['open', 'high', 'low', 'close', 'volume', 'volatility', 'ma_7', 'ma_30', 'cumulative_return']
    df = spark.createDataFrame([tuple(feature_list)], columns)

    # Predict
    predicted_row = model.transform(df).collect()[0]
    prediction = float(predicted_row.probability[1])  # Probability of positive class (label 1)


    return jsonify({'positive_return_probability': prediction})

if __name__ == '__main__':
    app.run(debug=True)
