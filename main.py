from deck import Deck
from players import Player


def main():
    deck = Deck()
    deck.shuffle()

    player = Player('Bryce')
    dealer = Player('Dealer')

    for _ in range(2):
        player.drawCard(deck.deal())
        dealer.drawCard(deck.deal())

        player.scoreKeeper()
        dealer.scoreKeeper()

        print(player)
        print(f'Player score: {player.score}')

        print(dealer)
        print(f'Dealer score: {dealer.score}')


if __name__ == '--main':
    main()
