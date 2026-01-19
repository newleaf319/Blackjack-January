from card import Card  # access the card class & its methods
import random

# deck class needs to know all possible card ranks & suits to build out every card


class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8',     # list of all possible suits & ranks
                      '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        self.cards = []  # prepares a place to store card instaces // actual deck

        # loops through and creates a Card instance & adds it to the deck
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    # randomly rearrange the deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
