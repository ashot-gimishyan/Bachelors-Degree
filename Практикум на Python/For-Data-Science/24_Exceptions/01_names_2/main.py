sym_sum = 0
string = 0

with open('people.txt', 'r') as file:
    for line in file:
        l = len(line) - 1
        string += 1
        sym_sum += l
        if (l < 3):
            try:
                raise BaseException("Ошибка в строке {}".format(string))
            except BaseException as e:
                print(e)

print(sym_sum)

