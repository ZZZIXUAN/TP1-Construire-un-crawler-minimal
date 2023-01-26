import unittest
from crawler import Crawler


class TestIsUrlInvalid(unittest.TestCase):

    def test_crawler(self):
        # Test du crawler à une profondeur de 50
        url = 'https://ensai.fr/'
        depth = 50
        obj = Crawler(url, depth)
        self.assertEqual(50, len(obj.crawled_urls))

    def test_crawler_empty_link(self):
        # Test du lien vide
        url = ''
        depth = 50
        obj = Crawler(url, depth)
        self.assertEqual(0, len(obj.crawled_urls))