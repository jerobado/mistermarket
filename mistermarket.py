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

    def __init__(self, ticker, market=None):

        self.ticker = ticker
        self.market = market
        self.company = None
        self.price = None
        self._search_ticker()

    def _search_ticker(self):

        try:

            if self.market == 'equity':
                self._search_equity()

            elif self.market == 'uitf':
                self._search_uitf()

        except Exception:
            return None

    def _search_uitf(self):

        uitf_url = 'http://www.uitf.com.ph/daily_navpu.php?bank_id=9#gsc.tab=0'  # landbank only
        response = requests.get(uitf_url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        fund_names = [element.a.get_text(strip=True) for element in
                      soup.find_all('td', attrs={'data-title': 'Fund Name'})]
        navpu = [float(element.div.get_text(strip=True)) for element in
                 soup.find_all('td', attrs={'data-title': 'NAVpu'})]

        landbank = dict(zip(fund_names, navpu))

        self.company = self.ticker
        self.price = landbank.get(self.ticker, None)

    def _search_equity(self):

        investegram_url = f'https://www.investagrams.com/stock/{self.ticker}'
        response = requests.get(investegram_url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        self.company = soup.find('h4', class_='mb-0').find('small').get_text(strip=True)
        self.price = float(soup.find(id="lblStockLatestLastPrice").get_text(strip=True))
