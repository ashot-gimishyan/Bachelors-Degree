alphabet = 'abcdefg'

#Копия строки
print(alphabet[:])

#Элементы строки в обратном порядке
print(alphabet[::-1])

#Каждый второй элемент строки (включая самый первый)
print(alphabet[::2])

#Каждый второй элемент строки после первого
print(alphabet[1::2])

#Все элементы до второго
print(alphabet[:1])

#Все элементы начиная с конца до предпоследнего
print(alphabet[-1::])

#Все элементы в диапазоне индексов от 3 до 4 (не включая 4)
print(alphabet[3:4])

#Последние три элемента строки
print(alphabet[:3:-1][::-1])

#Все элементы в диапазоне индексов от 3 до 4 (не включая 5)
print(alphabet[3:5])

#То же, что и в предыдущем, но выводится в обратном порядке.
print(alphabet[3:5][::-1])

#Все элементы начиная с предпоследнего с обратным  шагом 2
print(alphabet[-2::-2])

#То же, что и в предыдущем
print(alphabet[::-1][1::2])
