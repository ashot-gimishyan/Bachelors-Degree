members = []

n = int(input('Сколько всего человек? '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек\n')

out = 0
members = list(range(1, n + 1))
while len(members) > 1:

    print('Текущий круг людей:', members)
    start_count = out % len(members)
    out = (start_count + number - 1) % len(members)

    print('Начало счёта с номера', members[start_count])
    print('Выбывает человек под номером', members[out])
    print()

    members.remove(members[out])

print('Остался человек под номером', *members)
