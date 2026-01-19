class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __eq__(self, other):
        if not isinstance(other, Card):  # make sure other is a card
            return False
        return self.__dict__ == other.__dict__  # dunder attribute to bundle init

    def value(self):  # card finds it suit then returns its rank value
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)
