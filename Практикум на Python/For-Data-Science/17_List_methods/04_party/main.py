guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке {} человек: {}'.format(len(guests), guests))
    mes = input('Гость пришел или ушел? ')
    if mes == 'Пора спать':
        break

    name = input('Имя гостя: ')

    if mes == 'пришел':
        if len(guests) < 6:
            guests.append(name)
            print('Привет, {}!'.format(name))
        else:
            print('Прости, {}, но мест нет.'.format(name))
    elif mes == 'ушел':
        guests.remove(name)
        print('Пока, {}!'.format(name))
