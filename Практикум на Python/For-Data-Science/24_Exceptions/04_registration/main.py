good = open('registrations_good.log', 'a')
bad = open('registrations_bad.log', 'a')

with open('registrations.txt', 'r') as file:
    for line in file:
        line = line.split()
        already_written = False
        try:
            if (len(line) != 3):
                raise IndexError(' НЕ присутствуют все три поля\n')
        except IndexError as i:
            bad.write(' '.join(line) + str(i))
            continue
        else:
            good.write(' '.join(line) + '\n')
            already_written = True

        try:
            if (not line[0].isalpha()):
                raise NameError(' поле имени содержит НЕ только буквы\n')
        except NameError as n:
            bad.write(' '.join(line) + str(n))
            continue
        else:
            if already_written is False:
                good.write(' '.join(line) + '\n')

        try:
            if '@' not in line[1] or '.' not in line[1]:
                raise SyntaxError(' поле емейл НЕ содержит @ или .(точку)\n')
        except SyntaxError as s:
            bad.write(' '.join(line) + str(s))
            continue
        else:
            if already_written is False:
                good.write(' '.join(line) + '\n')

        try:
            if 10 > int(line[2]) or int(line[2]) > 99:
                raise ValueError(' поле возраст НЕ является числом от 10 до 99\n')
        except ValueError as v:
            bad.write(' '.join(line) + str(v))
        else:
            if already_written is False:
                good.write(' '.join(line) + '\n')