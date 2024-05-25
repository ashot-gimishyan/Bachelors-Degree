from blackjack import CardDeck, Player
from os import system, name


def cls():
    system('cls' if name == 'nt' else 'clear')


def print_player_state(player, mask=False):
    if not mask:
        print('{} hand: {}. Current score: {}'.format(
            player.get_name(),
            player.get_hand(),
            player.get_score()
        ))
    else:
        print('{} hand: {}. Current score: {}'.format(
            player.get_name(),
            '\U0001F0A0' * player.get_hand_count(),
            '?'
        ))


def player_win(player, dealer, bet):
    print('\033[1m\033[94mPlayer wins!\033[0m \U0001F911\n')
    player.change_balance(bet)
    dealer.change_balance(-bet)
    input('Press Enter...')
    return 0


def player_lose(player, dealer, bet):
    print('\033[1m\033[94mDealer wins!\033[0m \U0001F608\n')
    player.change_balance(-bet)
    dealer.change_balance(bet)
    input('Press Enter...')
    return 0


def play_round(player, dealer):
    while True:
        print('Input bet:', end=' ')
        try:
            bet = int(input())
        except ValueError:
            print('Must be integer value')
            continue
        if 0 < bet <= player.get_bank() and 0 < bet <= dealer.get_bank():
            print()
            break
        print('Not enough money to bet ...')
        print()

    deck = CardDeck()

    player.set_deck(deck=deck)
    dealer.set_deck(deck=deck)
    player.throw_hand()
    dealer.throw_hand()

    dealer.take_pair()
    player.take_pair()

    print('\033[1m\033[94mPlayer and Dealer took pairs\033[0m')
    print_player_state(player)
    print_player_state(dealer, mask=True)
    print()

    while True:
        if dealer.get_score() < 17:
            print('\033[1m\033[94mDealer took one more card ...\033[0m')
            dealer.take_card()
        print('Would you take another one? (1 - yes, 0 - cards out)', end=' ')
        new_choice = input()
        if new_choice == '0':
            while dealer.get_score() < 17:
                print('\033[1m\033[94mDealer took one more card ...\033[0m')
                dealer.take_card()
            print()
            break
        elif new_choice == '1':
            player.take_card()
            if player.get_score() > 21:
                break

        print()
        print_player_state(player)
        print_player_state(dealer, mask=True)

    print_player_state(player)

    if player.get_score() > 21:
        player_lose(player, dealer, bet)
        return 0

    print_player_state(dealer)

    if player.get_score() > dealer.get_score() or dealer.get_score() > 21:
        player_win(player, dealer, bet)
    elif player.get_score() < dealer.get_score():
        player_lose(player, dealer, bet)
    else:
        print('\033[1m\033[94mIts draw \U0001F44D\n')
        input('Press Enter...')

    del deck
    return 0


def main():
    sep = '\u23BA\u23BB\u23BC\u23BD\u23BC\u23BB\u23BA' * 6
    bank = int(input('Input bank: '))
    me = Player(name='Alex', money=bank)
    dealer = Player(name='Dealer', money=bank)

    turn = 1
    while True:
        cls()
        print('\033[1m\033[92mBLACKJACK\033[0m \U0001F44D')
        print(sep)
        print('\033[1m\033[94mRound {}. {} bank: {}. {} bank: {}\033[0m'.format(
            turn,
            me.get_name(),
            me.get_bank(),
            dealer.get_name(),
            dealer.get_bank()
        ))
        print('Start Round - 1\nExit - 2\n')
        choice = input('Your choice: ')
        if choice == '2':
            break
        elif choice == '1':
            play_round(me, dealer)
            turn += 1

        if dealer.get_bank() == 0:
            print('\033[1m\033[94mYOU WON THE GAME \U0001F44D\n')
            break
        if me.get_bank() < 10:
            print('\033[1m\033[94mCHEAT +1000 ON YOUR ACCOUNT \U0001F44D\n')
            me.change_balance(1000)

    return 0


main()