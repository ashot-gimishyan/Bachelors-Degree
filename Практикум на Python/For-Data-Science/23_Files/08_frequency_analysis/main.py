file = open('text.txt', 'r')
analysis = open('analysis.txt', 'w')


text = file.read()
count = 0
alpha_dct = {}


for sym in text:
    if sym.isalpha():
        count += 1
        sym = sym.lower()
        if sym in alpha_dct:
            alpha_dct[sym] += 1
        else:
            alpha_dct[sym] = 1


lst = []
for key, value in alpha_dct.items():
    n = f"{value/ count:.3f}"
    tmp = (key, n)
    lst.append(tmp)


lst = sorted(lst, key = lambda x: (x[0]), reverse=False)
lst = sorted(lst, key = lambda x: (x[1]), reverse=True)


for data in lst:
    analysis.write(data[0] + " " + data[1] + '\n')


file.close()
analysis.close()