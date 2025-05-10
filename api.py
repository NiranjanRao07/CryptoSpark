from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.regression import LinearRegressionModel

# Start Spark
spark = SparkSession.builder.appName("ModelAPI").getOrCreate()

# Load model
model = LinearRegressionModel.load("C:/SJSU/Spring_2025/Big_Data_Technologies/Group_Project/GitHub_Repo/CryptoSpark/linearRegression_model")

# Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    feature_list = data['features']  # List of 14 numeric values

    # Create DataFrame with features
    df = spark.createDataFrame([(Vectors.dense(feature_list),)], ["features"])

    # Predict
    prediction = model.transform(df).collect()[0].prediction

    return jsonify({'daily_return': prediction})

if __name__ == '__main__':
    app.run(debug=True)
