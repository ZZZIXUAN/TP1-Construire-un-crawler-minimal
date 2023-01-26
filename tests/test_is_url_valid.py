import unittest
from helpers import is_url_valid


class TestIsUrlValid(unittest.TestCase):

    def test_is_url_valid_with_pdf(self):
        # Test si url valide avec pdf
        link = 'https://ensai.fr/wp-content/uploads/2021/10/plaquette-ENSAI-2022.pdf'
        truth_value = is_url_valid(link)
        self.assertFalse(truth_value)

    def test_is_url_valid_empty_link(self):
        # Test si url valide avec le lien vide
        link = ''
        truth_value = is_url_valid(link)
        self.assertFalse(truth_value)

    def test_is_url_valid_fragments(self):
        # Test si les fragments d'url valide
        valid_link = 'https://ensai.fr/#about_us'
        truth_value = is_url_valid(valid_link)
        self.assertFalse(truth_value)
