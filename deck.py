import random  # needed to shuffle cards
from card import Card  # access the card class & its methods

# deck class needs to know all possible card ranks & suits to build out every card


class Deck:
    def __init__(self):
        # list of all possible suits & ranks
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8',
                      '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        self.cards = []  # prepares a place to store card instaces // actual deck

        # loops through and creates a Card instance & adds it to the deck
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    # randomly rearrange the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # take last card out deck and return it to whoever called the method
    # without return keyword no value is passed back only gets removed
    def deal(self):
        return self.cards.pop()


# instance of a deck
deck = Deck()

# have to use print to display return values
print(deck.deal())
