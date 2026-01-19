class Player:

    def __init__(self, name='bryce'):
        self.name = name
        self.hand = []
        self.score = 0

    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards in hand'

    def drawCard(self, card):
        self.hand.append(card)

    def discardCard(self, cardIdx):
        return self.hand.pop(cardIdx)

    def scoreKeeper(self):
        total = 0
        ace_count = 0

        for card in self.hand:  # loop through each card object in my hand
            total += card.value()  # add each cards value to total

            if card.rank == 'Ace':  # is this card an ace? if so
                ace_count += 1  # count the ace so it can be used later if needed

        while total > 21 and ace_count > 0:  # long as the loop statement conditions is true
            total -= 10  # lowers total by 10 (ace goes from 11 to 1)
            ace_count -= 1  # use up one ace adjustment

        self.score = total  # save final calculated score
