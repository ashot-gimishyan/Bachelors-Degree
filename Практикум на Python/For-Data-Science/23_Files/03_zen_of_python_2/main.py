zen = open('zen.txt', 'r')

lines = 0
latin = 0
words = 0

zen_dct = {}

for line in zen:
    lines += 1
    line = line.split()
    words += len(line)
    #print(words)
    for word in line:
        for sym in word:
            if sym.isalpha():
                latin += 1
                if sym in zen_dct:
                    zen_dct[sym] += 1
                else:
                    zen_dct[sym] = 1

zen.close()
print(lines, latin, words)

min_sym = None
min_count = None
min_count = min(zen_dct.values())

# наименьшее количество раз встречаются несколько букв
for i, j in zen_dct.items():
    if j == min_count:
        print(i)