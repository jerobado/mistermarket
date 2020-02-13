import unittest
import bs4
import requests
from mistermarket import MrMarket


class MrMarketTestCase(unittest.TestCase):

    def test_name_if_equal_to_ticker(self):

        company = MrMarket('jfc')
        result = company.ticker
        expected = 'jfc'

        self.assertEqual(result, expected)

    def test_search_ticker(self):

        ticker = 'jfc'
        company = MrMarket(ticker)

        investegram_url = f'https://www.investagrams.com/stock/{ticker}'
        response = requests.get(investegram_url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        expected = float(soup.find(id='lblStockLatestLastPrice').text.strip())
        print(f'{ticker} current price: {expected}')
        result = company.price

        self.assertEqual(result, expected, f'current price: {expected}')

    def test_price_return_type_equal_to_float(self):

        stock = MrMarket('ans')
        result = stock.price
        expected = float

        self.assertIsInstance(result, expected)

    def test_search_UITFPH_result(self):

        ticker = 'LANDBANK Money Market Plus Fund'
        url = {'LANDBANK Money Market Plus Fund': 'http://www.uitf.com.ph/daily_navpu.php?bank_id=9#gsc.tab=0'}
        response = requests.get(url[ticker])
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        fund_names = [element.a.get_text(strip=True) for element in soup.find_all('td', attrs={'data-title': 'Fund Name'})]
        navpu = [element.div.get_text(strip=True) for element in soup.find_all('td', attrs={'data-title': 'NAVpu'})]

        landbank = dict(zip(fund_names, navpu))

        for fund, navpu in landbank.items():
            print(fund, navpu)

        # latest navpu of ticker
        print(landbank.get(ticker, None))


if __name__ == '__main__':
    unittest.main()
