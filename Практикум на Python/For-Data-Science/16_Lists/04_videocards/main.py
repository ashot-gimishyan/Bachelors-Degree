'''

Кол-во видеокарт: 5
1 Видеокарта: 3070
2 Видеокарта: 2060
3 Видеокарта: 3090
4 Видеокарта: 3070
5 Видеокарта: 3090

Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
Новый список видеокарт: [ 3070 2060 3070 ]
'''

n = int(input('Кол-во видеокарт: '))

v = []
for i in range(n):
    print(i+1, 'Видеокарта:', end=" ")
    val = int(input())
    v.append(val)

max_in_v = max(v)
max_count = v.count(max_in_v)

print(*v)

for _ in range(max_count):
    v.remove(max_in_v)

print(*v)
