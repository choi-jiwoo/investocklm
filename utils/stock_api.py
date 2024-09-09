import streamlit as st
import finnhub
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class StockAPI(ABC):

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def api_key(self) -> str:
        return self._api_key
    
    @api_key.setter
    def api_key(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('API Key should be provided in string object')
        self._api_key = value

    @abstractmethod
    def initialize(self):
        pass

class Finnhub(StockAPI):

    def initialize(self):
        self.client = finnhub.Client(api_key=self.api_key)

    @st.cache_resource
    def get_news(_self, ticker: str, days: int=5, max_: int=10):
        print(f'Getting {ticker} news...')
        today = datetime.today()
        b4_5d = today - timedelta(days=days)
        _from = b4_5d.strftime('%Y-%m-%d')
        to = today.strftime('%Y-%m-%d')
        print(f'/company-news?symbol={ticker}&from={_from}&to={to}')
        news = _self.client.company_news(ticker, _from=_from, to=to)
        return news[:max_]
