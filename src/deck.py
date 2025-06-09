import random
from card import Card
class Deck:
    def __init__(self):
        """A standard deck has 52 cards"""
        self.cards = [Card(suit, rank) for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades'] for rank in
                      ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']]
        self.drawn_count = 0


    def deck_shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        """this method allows to keep track of card on top of the deck
        and also preserves the entire deck"""
        assert self.drawn_count < 53, "cannot draw from an empy deck!"
        drawn_card = self.cards[self.drawn_count]
        self.drawn_count += 1
        return drawn_card

    def cards_left(self):
        return 52 - self.drawn_count

    def cards_drawn(self):
        return self.drawn_count

    def reset_deck(self):
        self.drawn_count = 0
        self.deck_shuffle()













