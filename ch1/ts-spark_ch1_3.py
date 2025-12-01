# Databricks notebook source
import numpy as np
from plotly.subplots import make_subplots

time_period = np.arange(0, 12, 1/365)

(amp, freq) = (3, 0.33)
seasonality1 = amp * np.sin(2 * np.pi * freq * time_period)
(amp, freq) = (2, 1)
seasonality2 = amp * np.sin(2 * np.pi * freq * time_period)
(amp, freq) = (1, 4)
seasonality3 = amp * np.sin(2 * np.pi * freq * time_period)

combined = seasonality1 + seasonality2 + seasonality3

fig = make_subplots(rows=4, cols=1, shared_xaxes=True)
fig.add_scatter(x=time_period, y=seasonality1, row=1, col=1, name=f"seasonality 1")
fig.add_scatter(x=time_period, y=seasonality2, row=2, col=1, name=f"seasonality 2")
fig.add_scatter(x=time_period, y=seasonality3, row=3, col=1, name=f"seasonality 3")
fig.add_scatter(x=time_period, y=combined, row=4, col=1, name=f"combined")
fig.show()