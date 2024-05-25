vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = input('Введите текст: ')
lst = [x for x in text if x in vowels]
print('Список гласных букв:', lst)
print('Длина списка:', len(lst))