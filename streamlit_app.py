import streamlit as st
from utils.stock_api import Finnhub
import os


def get_news(ticker: str):
    ticker = ticker.upper()
    st.markdown(f'# {ticker}')
    market_news = client.get_news(ticker, days=5, max_=10)
    
    st.markdown('### Latest News')
    
    container = st.container(border=True)

    for news in market_news:
        url = news['url']
        headline = news['headline']
        summary = news['summary']
        html_link = f'<a href="{url}" target="_blank">{headline}</a>'
        container.markdown(html_link, unsafe_allow_html=True)
        container.caption(summary)

st.set_page_config('Home')

style = """
<style>
  a {
    text-decoration: none;
    color: #ffffff !important;
  }
  a:hover {
    font-weight: bold;
  }
</style>
"""
st.markdown(style, unsafe_allow_html=True)
ticker = st.sidebar.text_input('Enter Ticker', placeholder='Ticker')
st.sidebar.button('Submit', on_click=get_news, args=(ticker,))

api_key = os.environ['FINNHUB_APIKEY']
client = Finnhub(api_key)
client.initialize()

