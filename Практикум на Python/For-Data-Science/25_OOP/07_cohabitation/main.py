from person import Person
from house import House
from random import randint


def spend_day(player, number):
    print(player.get_name(), end=' | ')
    if player.get_fullness() < 20:
        print('Action: going to eat ...')
        player.eat()
    elif house.get_food() < 10:
        print('Action: go shopping ...')
        player.go_shopping()
    elif house.get_money() < 50:
        print('Action: go to work ...')
        player.work()
    elif number == 1:
        print('Action: Oh no, another day on work ...')
        player.work()
    elif number == 2:
        print('Action: Going to eat ...')
        player.eat()
    else:
        player.play()

    return 0


house = House()
player1 = Person(name='Igor', house=house)
player2 = Person(name='Victoria', house=house)
day = 1

while day <= 365:

    print('\033[1m\033[92mDay №{}\033[0m \U0001F4C6'.format(day))

    spend_day(player1, randint(1, 6))
    spend_day(player2, randint(1, 6))

    print('-' * 30)
    print(player1)
    print(player2)

    if not player1.is_alive():
        print('\033[1m\033[91mExperiment is over. {} is dead\033[0m \U0001F608'.format(player1.get_name()))
        break
    if not player2.is_alive():
        print('\033[1m\033[91mExperiment is over. {} is dead\033[0m \U0001F608'.format(player2.get_name()))
        break
    day += 1
    print()

if day == 366:
    print('OK')

