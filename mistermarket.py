"""
Mr. Market - your servant in the Philippine financial market

Features & Benefits
* Get the latest market price of a stock in the Philippine Stock Exchange

Usage
> from mistermarket import MrMarket
> jfc = MrMarket('jfc') # accepts stock ticker
> meg = MrMarket('meg')
> jfc.price
119.32
> meg.price
3.75

"""

__version__ = '0.1'

import bs4
import requests


class MrMarket:

    def __init__(self, ticker):

        self.name = ticker
        self.price = self._search_ticker()

    def _search_ticker(self):

        try:
            result = None
            investegram_url = f'https://www.investagrams.com/stock/{self.name}'
            response = requests.get(investegram_url)
            soup = bs4.BeautifulSoup(response.content, 'html.parser')
            result = soup.find(id="lblStockLatestLastPrice").text.strip()
            return float(result)

        except Exception:
            return None
