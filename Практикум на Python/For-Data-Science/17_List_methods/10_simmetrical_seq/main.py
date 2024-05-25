
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print('Последовательность:', *arr)

i = 0
while arr != arr[::-1]:
    arr.insert(n, arr[i])
    i += 1

print('Нужно приписать чисел:', i)
print('Сами числа:', *arr[:i][::-1])
