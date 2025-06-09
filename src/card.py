
class Card:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    suit_symbols = {'Clubs': '♣', 'Diamonds': '♦', 'Hearts': '♥', 'Spades': '♠'}
    rank_values = {rank: i + 2 for i, rank in enumerate(ranks)}
    suit_values = {suit: i for i, suit in enumerate(suits)}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def rank_value(self):
        return Card.rank_values[self.rank]

    def suit_value(self):
        return Card.suit_values[self.suit]

    def card_rank(self):
        return self.rank

    def card_suit(self):
        return self.suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def show(self):
        return f'{self.rank}{Card.suit_symbols[self.suit]}'

'''
myCard = Card('Spades', 'A')
print(myCard.rank_values)
'''

