n = int(input('Кол-во контейнеров: '))

c = []
for i in range(n):
    w = int(input('Введите вес контейнера: '))
    c.append(w)

new = int(input('Введите вес нового контейнера: '))

index = 1
for el in c:
    if el >= new:
        index += 1
        continue
    break

print('Номер, куда встанет новый контейнер:', index)