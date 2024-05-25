countries_num = int(input("Количество стран: "))

countries = dict()
for i in range(countries_num):
    print("{0} страна: ".format(i+1), end="")
    s = input().split()
    countries[s[0]] = s[1:]


for i in range(3):
    print("{0} город: ".format(i+1), end="")
    c = input()

    for k in countries.keys():
        if c in countries[k]:
            print("Город {0} расположен в стране {1}.".format(c, k))
            break
    else:
       print(f'По городу {c} данных нет.')