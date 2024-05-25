s1 = input()
s2 = input()

n = len(s2)
flag = True

for i in range(n):
    s2 = s2[-1:] + s2[:-1]
    if s1 == s2:
        print('Первая строка получается из второй со сдвигом {}'.format(i+1))
        flag = True
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
