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

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()

    if 'Date' in data.columns and 'Close' in data.columns:
        df_train = data[['Date','Close']].copy() # Use .copy() to avoid SettingWithCopyWarning
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        st.subheader('Forecast data')
        st.write(forecast.tail())

        st.write(f'Forecast plot for {n_years} years')
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        st.write("Forecast components")
        fig2 = m.plot_components(forecast)

        st.pyplot(fig2)
    else:
        st.error("Could not find 'Date' or 'Close' columns in the data. Check data loading.")
        
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.error("Check if the stock ticker is valid and data is available.")    