number_max = int(input('Введите максимальное число: '))
numbers_plenty = set(range(1, number_max + 1))

while True:
    numbers = input('Нужное число есть среди вот этих чисел: ')
    if numbers == 'Помогите!':
        print('Артем мог загадать следующие числа:', *numbers_plenty)
        break
    else:
        new_numbers_plenty = set(map(int, numbers.split()))

    if input('Ответ Артема: ') == 'Да':
        numbers_plenty &= new_numbers_plenty
    else:
        numbers_plenty -= new_numbers_plenty