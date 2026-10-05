import unittest
from scripts.check_brand_alignment import check

class BrandAlignmentTests(unittest.TestCase):
    def test_canonical_tokens_and_historical_rules(self):
        self.assertEqual(check(), [])
