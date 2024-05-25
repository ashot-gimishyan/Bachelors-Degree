def get_index(smb, to_right, lst):
    index = lst.index(smb)
    if index + to_right > len(lst) - 1:
        return index + to_right - len(lst)

    return index + to_right

text = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

alpha = [chr(i) for i in range(ord('а'), ord('я') + 1)]
result = ''

for symbol in text:
    if symbol in alpha:
        result += alpha[get_index(symbol, shift, alpha)]
    else:
        result += symbol

print('Зашифрованное сообщение: ', result)