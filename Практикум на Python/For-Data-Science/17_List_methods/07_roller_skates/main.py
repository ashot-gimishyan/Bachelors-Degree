c_list = list()
p_list = list()

n = int(input('Кол-во коньков: '))
for i in range(n):
    print('Размер {} пары: '.format(i+1),end="")
    tmp = int(input())
    c_list.append(tmp)

m = int(input('Кол-во людей: '))
for i in range(m):
    print('Размер ноги {} человека: '.format(i+1),end="")
    tmp = int(input())
    p_list.append(tmp)

count = 0
m = min(p_list)

# удалим все пары, которые точно не подойдут
for i in range(len(c_list)):
    if c_list[i - count] < m:
        c_list.remove(c_list[i - count])
        count += 1

print(min(len(p_list), len(c_list)))
