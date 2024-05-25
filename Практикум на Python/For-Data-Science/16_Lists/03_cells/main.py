n = int(input('Кол-во клеток: '))

invalid_values = list()

for i in range(n):
    print('Эффективность', i+1, 'клетки:', end=" ")
    value = int(input())
    if value < i + 1:
        invalid_values.append(value)

print('Неподходящие значения:', *invalid_values)