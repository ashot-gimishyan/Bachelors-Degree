word = input('Введите слово: ')

unique = 0
for sym in word:
    if word.count(sym) == 1:
        unique += 1

print('Кол-во уникальных букв:', unique)