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

    def test_bloomberg_url(self):

        # [] TODO: learn how to interact with webpage bot inspectors
        ticker = 'LBMMKPL'
        bloomberg_url = f'https://www.bloomberg.com/quote/{ticker}:PM'
        print(bloomberg_url)
        response = requests.get(bloomberg_url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())
        # result = soup.find_all(class_='priceText__1853e8a5')
        # print(result)

        # self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
