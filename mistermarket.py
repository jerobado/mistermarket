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

        self.company = str
        self.price = float
        self.ticker = ticker
        self._search_ticker(ticker)

    def _search_ticker(self, ticker):

        try:
            investegram_url = f'https://www.investagrams.com/stock/{ticker}'
            response = requests.get(investegram_url)
            soup = bs4.BeautifulSoup(response.content, 'html.parser')
            self.company = soup.find('h4', class_='mb-0').find('small').get_text(strip=True)
            self.price = float(soup.find(id="lblStockLatestLastPrice").get_text(strip=True))

        except Exception:
            return None
