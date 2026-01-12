class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # best way to display objects with text instead of memory address representation
    def __str__(self):
        return f'{self.rank} of {self.suit}'

    # value comparison overall scope
    def __eq__(self, other):
        # if the other thing is not a card they are not equal
        if not isinstance(other, Card):
            return False
        # cards are equal if the rank & suit match
        return self.rank == other.rank and self.suit == other.suit

    # returns the blackjack value of this card
    def value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)
