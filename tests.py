import unittest
import bs4
import requests
from mistermarket import MrMarket


class MrMarketTestCase(unittest.TestCase):

    def test_init_arguments(self):

        company = MrMarket('jfc', market='equity')
        result_company = company.ticker
        result_market = company.market
        expected_company = 'jfc'
        expected_market = 'equity'

        self.assertEqual(result_company, expected_company)
        self.assertEqual(result_market, expected_market)

    def test_search_equity(self):

        ticker = 'jfc'
        company = MrMarket(ticker, market='equity')

        investegram_url = f'https://www.investagrams.com/stock/{ticker}'
        response = requests.get(investegram_url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        expected = float(soup.find(id='lblStockLatestLastPrice').text.strip())
        result = company.price

        self.assertEqual(result, expected, f'current price: {expected}')

    def test_price_return_type_equal_to_float(self):

        stock = MrMarket('ans', market='equity')
        uitf = MrMarket('LANDBANK Equity Fund', market='uitf')
        result_stock = stock.price
        result_uitf = uitf.price
        expected = float

        self.assertIsInstance(result_stock, expected)
        self.assertIsInstance(result_uitf, expected)

    def test_search_uitf(self):

        ticker = 'LANDBANK Money Market Plus Fund'
        uitf_url = 'http://www.uitf.com.ph/daily_navpu.php?bank_id=9#gsc.tab=0'  # landbank
        response = requests.get(uitf_url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        fund_names = [element.a.get_text(strip=True) for element in
                      soup.find_all('td', attrs={'data-title': 'Fund Name'})]
        navpu = [float(element.div.get_text(strip=True)) for element in
                 soup.find_all('td', attrs={'data-title': 'NAVpu'})]

        landbank = dict(zip(fund_names, navpu))

        self.price = landbank.get(ticker, None)


if __name__ == '__main__':
    unittest.main()
