import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

start = "2015-01-01"
Today = date.today().strftime("%Y-%m-%d")

st.title("Stock Forecast App")

stocks =st.text_input('Enter Stock Symbol', 'GOOG')
selected_stock = st.selectbox('Selected dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

