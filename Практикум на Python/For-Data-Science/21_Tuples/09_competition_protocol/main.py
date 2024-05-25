N = int(input("Сколько записей вносится в протокол? "))

print("Записи (результат и имя): ")
win1 = dict()
win2 = dict()
win3 = dict()

max1 = 0
max2 = 0
max3 = 0

for i in range(N):
    print("{i} запись: ".format(i=i+1), end='')
    score, name = input('').split()
    score = int(score)
    if score > max1:
        max1 = score
        if win1.keys():
            win1.clear()
            win1[name] = score
        else:
            win1[name] = score
    elif score > max2:
        max2 = score
        if win2.keys():
            win2.clear()
            win2[name] = score
        else:
            win2[name] = score
    elif score > max3:
        max3 = score
        if win3.keys():
            win3.clear()
            win3[name] = score
        else:
            win3[name] = score
    else:
        continue
print(win1, win2, win3)