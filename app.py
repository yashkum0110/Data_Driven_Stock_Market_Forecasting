import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

start = "2015-01-01"
Today = date.today().strftime("%Y-%m-%d")