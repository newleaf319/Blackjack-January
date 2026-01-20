# imported classes
from deck import Deck
from players import Player


def main():
    # make a new deck & mix it up
    deck = Deck()
    deck.shuffle()

    # created players
    player = Player('Bryce')
    dealer = Player('Dealer')

    # bet your money
    print(f"Available Currencies: {', '.join((player.money.RATES.keys()))}")
    new_currency = input('Choose your currency:').upper()
    player.money.convert_to(new_currency)

    print(player.money)

    bet = float(input('Place your bet:'))
    player.money.subtract(bet)

    # deal starting cards (2 each)
    for i in range(2):
        player.drawCard(deck.deal())
        dealer.drawCard(deck.deal())

        # calculate both scores
        player.scoreKeeper()
        dealer.scoreKeeper()

    #  PLAYER TURN
    while True:
        print('\nYour hand:')
        print(player)
        print(f'Score: {player.score}')

        if player.score > 21:
            print('You busted!')
            break

        choice = input('Hit or stand? (h/s):').lower()
        if choice == 'h':
            player.drawCard(deck.deal())
            player.scoreKeeper()
        elif choice == 's':
            break
        else:
            print('Invalid choice.')

    # DEALER TURN (only plays if i bust)
    if player.score <= 21:
        print('\nDealer\'s turn')
        while dealer.score < 17:
            dealer.drawCard(deck.deal())
            dealer.scoreKeeper()

        print(dealer)
        print(f'Dealer score: {dealer.score}')

    # RESULTS
    print('\n--- FINAL RESULTS ---')
    if player.score > 21:
        print('Dealer wins! You busted.')
        player
    elif dealer.score > 21:
        print('You win! Dealer busted.')
    elif player.score > dealer.score:
        print('Youn win!')
    elif player.score < dealer.score:
        print('Dealer wins!')
    else:
        print('Push (tie).')


# only run main() when this file is the one i execute
if __name__ == '__main__':
    main()

main()
