# Databricks notebook source
from pyspark import SparkFiles
import pyspark.pandas as ps
import plotly.express as px
import pandas as pd

DATASET_FILE = "ts-spark_ch1_ds1.csv"
DATASET_URL = f"https://raw.githubusercontent.com/PacktPublishing/Time-Series-Analysis-with-Spark/main/ch1/{DATASET_FILE}"

# option 1 - using sparkContext
#spark.sparkContext.addFile(DATASET_URL)
#df1 = spark.read.format("csv").option("header", "true").load("file:///" + SparkFiles.get(DATASET_FILE))
# option 2 - using pandas
df1 = spark.createDataFrame(pd.read_csv(DATASET_URL))
#

df1.createOrReplaceTempView("temperatures")

df2 = spark.sql("select to_date(Category) as year, float(`Annual Mean`) as annual_mean from temperatures where Category > '1950'")
df2_pd = df2.toPandas()
df2_pd['year'] = ps.to_datetime(df2_pd['year'])
#display(df2_pd)

fig = px.scatter(df2_pd, x="year", y="annual_mean", trendline="ols", title='Average Temperature - Mauritius (from 1950)')
fig.update_traces(mode = 'lines')
fig.data[-1].line.color = 'red'
fig.data[-1].line.dash = 'dash'
fig.show()