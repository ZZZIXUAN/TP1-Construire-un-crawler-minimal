import unittest
from helpers import get_clean_url


class TestGetCleanUrl(unittest.TestCase):

    def test_get_clean_url_relative_url(self):
        # Test de l'URL relative
        link = '/en'
        parent_url = 'https://ensai.fr'
        complete_url = get_clean_url(parent_url, link)
        self.assertEqual('https://ensai.fr/en', complete_url)

    def test_get_clean_url_remove_slashes(self):
        # Test de suppression du slash
        link = '//en'
        parent_url = 'https://ensai.fr'
        complete_url = get_clean_url(parent_url, link)
        self.assertEqual('https://ensai.fr/en', complete_url)

    def test_get_clean_url_remove_empty_link(self):
        # Test de suppression des liens vide
        parent_url = 'https://ensai.fr'
        complete_url = get_clean_url(parent_url, '')
        self.assertEqual('https://ensai.fr', complete_url)
