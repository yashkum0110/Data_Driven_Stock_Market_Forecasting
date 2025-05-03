import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Forecast App")

stocks =st.text_input('Enter Stock Symbol', 'GOOG')
selected_stock = st.selectbox('Selected dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')

try:
    data = load_data(selected_stock)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1) 
        data = data.rename(columns={'':'Date'}) 
    data_load_state.text('Loading data... done!')

    st.subheader('Raw data')
    st.write(data.tail())

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.error("Check if the stock ticker is valid and data is available.")    