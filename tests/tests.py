import unittest
import bs4
import requests
from mistermarket.mistermarket import MrMarket


class MrMarketTestCase(unittest.TestCase):

    def test_init_arguments(self):

        company = MrMarket('jfc', market='equity')
        result_company = company.ticker
        result_market = company.market
        expected_company = 'jfc'
        expected_market = 'equity'

        self.assertEqual(result_company, expected_company)
        self.assertEqual(result_market, expected_market)

    def test_phisix_api_url(self):

        ticker = 'meg'
        quote = MrMarket(ticker)
        self.assertEqual(quote._status_code, 200)
        self.assertEqual(type(quote._json), dict)


if __name__ == '__main__':
    unittest.main()
