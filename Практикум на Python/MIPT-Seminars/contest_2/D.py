i = int(input())  # номер простого числа, которое хотим найти
n = 2 
count = 0  # количество делителей для каждого числа в конце цикла обнуляется
find_prost = 0  # сколько простых чисел найдено на данный момент

while True:
    for j in range(2, int(n**0.5) + 1):
        if (n % j == 0):
            count += 1
    if count == 0:
        find_prost += 1
    if find_prost == i:
        break
    count = 0
    n += 1
print(n)
