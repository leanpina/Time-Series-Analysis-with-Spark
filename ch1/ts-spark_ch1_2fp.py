# Databricks notebook source
pip install prophet

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from pyspark import SparkFiles
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import pandas as pd

DATASET_FILE = "ts-spark_ch1_ds2.csv"
DATASET_URL = f"https://raw.githubusercontent.com/PacktPublishing/Time-Series-Analysis-with-Spark/main/ch1/{DATASET_FILE}"

# option 1 - using sparkContext
#spark.sparkContext.addFile(DATASET_URL)
#df1 = spark.read.format("csv").option("header", "true").load("file:///" + SparkFiles.get(DATASET_FILE))
# option 2 - using pandas
df1 = spark.createDataFrame(pd.read_csv(DATASET_URL))
#

df1.createOrReplaceTempView("temperatures")

df2 = spark.sql("select to_date(date) as ds, float(daily_min_temperature) as y from temperatures sort by ds asc")
df2_pd = df2.toPandas()
#display(df2_pd)

model = Prophet(n_changepoints=20, yearly_seasonality=True, changepoint_prior_scale=0.001)
model.fit(df2_pd)

future_dates = model.make_future_dataframe(periods=365, freq='D')
forecast = model.predict(future_dates)

plot_plotly(model, forecast, changepoints=True)

# COMMAND ----------

plot_components_plotly(model, forecast)