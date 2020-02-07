import unittest
import bs4
import requests
from mistermarket import MrMarket


class MrMarketTestCase(unittest.TestCase):

    def test_name_if_equal_to_ticker(self):

        company = MrMarket('jfc')
        result = company.name
        expected = 'jfc'

        self.assertEqual(result, expected)

    def test_search_ticker(self):

        ticker = 'jfc'
        company = MrMarket(ticker)

        investegram_url = f'https://www.investagrams.com/stock/{ticker}'
        response = requests.get(investegram_url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        expected = float(soup.find(id='lblStockLatestLastPrice').text.strip())
        print(f'current price: {expected}')
        result = company._search_ticker()

        self.assertEqual(result, expected, f'current price: {expected}')


if __name__ == '__main__':
    unittest.main()
