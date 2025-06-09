import unittest
from src.card import Card


class TestCard(unittest.TestCase):
    def test_card_repr(self):
        card = Card('Spades', 'A')
        #print(repr(card))
        print(card.rank_value())
        self.assertEqual(repr(card), 'A of Spades')
        self.assertEqual('A♠', card.show())

    def test_card_ordering(self):
        card1 = Card('A', 'Clubs')
        card2 = Card('K', 'Spades')
        self.assertTrue(card1 > card2)  # Assuming __lt__ is implemented

    def test_invalid_rank(self):
        with self.assertRaises(AssertionError):
            Card('1', 'Hearts')

if __name__ == '__main__':
    unittest.main()
