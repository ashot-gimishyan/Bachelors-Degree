dct = {}

n = int(input('Введите количество пар слов: '))

for i in range(n):
    print(f"{i+1} пара: ", end="")
    pair = input().split()
    dct[pair[0]] = pair[2]


while True:
    word = input('Введите слово: ')
    word = word.title()
    if word in dct.keys():
        print('Синоним: ', dct[word])
    elif word in dct.values():
        for key in dct:
            if dct[key] == word:
                print('Синоним: ', key)
                break
    else:
        print('Такого слова в словаре нет.')