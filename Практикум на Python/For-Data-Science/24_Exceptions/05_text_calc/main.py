def IsValueErr(a, b):
    try:
        float(a)
        float(b)
    except ValueError:
        print("Не число")
        return True
    else:
        return False


def IsZeroDiv(a, b):
    try:
        float(a) / float(b)
    except ZeroDivisionError:
        print("Деление на ноль")
        return True
    else:
        return False

summa = 0
with open('calc.txt', 'r') as calc:
    for line in calc:

        line = line.split()

        if IsValueErr(line[0], line[2]):
            continue

        try:
            if len(line[1]) >= 2 and line[1] != "//" and line[1] != "**":
                raise ArithmeticError("Ошибка арифметического знака")
        except ArithmeticError as a:
            print(a)
            continue


        if '.' not in line[0]:
            type1 = int
        else:
            type1 = float

        if '.' not in line[2]:
            type2 = int
        else:
            type2 = float

        if line[1] == '*':
            summa += type1(line[0]) * type2(line[2])

        elif line[1] == '+':
            summa += type1(line[0]) + type2(line[2])

        elif line[1] == '-':
            summa += type1(line[0]) - type2(line[2])

        elif line[1] == '/':
            if IsZeroDiv(line[0], line[2]):
                continue
            summa += type1(line[0]) / type2(line[2])

        elif line[1] == '%':
            if IsZeroDiv(line[0], line[2]):
                continue
            summa += type1(line[0]) % type2(line[2])

        elif line[1] == '//':
            if IsZeroDiv(line[0], line[2]):
                continue
            summa += type1(line[0]) // type2(line[2])

        elif line[1] == '**':
            summa += type1(line[0]) ** type2(line[2])

print(summa)
