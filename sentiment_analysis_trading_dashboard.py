import streamlit as st
import pandas as pd
import yfinance as yf
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI

# Define function to get stock data
@st.cache_data
def get_stock_data(ticker):
    data = yf.download(ticker, period="1d", interval="1m")
    return data

# Define function to get crypto data
@st.cache_data
def get_crypto_data(id):
    cg = CoinGeckoAPI()
    data = cg.get_coin_market_chart_by_id(id, vs_currency="usd", days=1)
    data = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    data["timestamp"] = pd.to_datetime(data["timestamp"], unit="ms")
    data = data.set_index("timestamp")
    return data

# Define function to get news sentiment
@st.cache_data
def get_news_sentiment(query):
    url = f"https://newsapi.org/v2/everything?q={query}&amp;from=2022-04-01&amp;to=2022-04-14&amp;sortBy=popularity&amp;apiKey=YOUR_API_KEY"
    data = pd.read_json(url)
    data["sentiment"] = data["description"].apply(lambda x: TextBlob(x).sentiment.polarity)
    return data

# Define sidebar
st.sidebar.title("Select Asset")
assets = {"Stocks": ["AAPL", "MSFT", "GOOG"], "Crypto": ["bitcoin", "ethereum", "dogecoin"]}
selected_asset_type = st.sidebar.selectbox("Select asset type", list(assets.keys()))
selected_asset = st.sidebar.selectbox("Select asset", assets[selected_asset_type])

# Display asset price data
st.title(f"{selected_asset_type} Price Data")
if selected_asset_type == "Stocks":
    data = get_stock_data(selected_asset)
    st.line_chart(data["Close"])
else:
    data = get_crypto_data(selected_asset)
    st.line_chart(data)

# Display news sentiment data
st.title("News Sentiment Data")
news_data = get_news_sentiment(selected_asset)
st.write(news_data)
sns.histplot(data=news_data, x="sentiment")
st.pyplot()
