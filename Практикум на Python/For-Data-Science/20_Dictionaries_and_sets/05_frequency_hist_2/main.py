text = input()

dct = dict()
for sym in text:
    if sym in dct:
        dct[sym] += 1
    else:
        dct[sym] = 1

max_val = max(dct.values())

new_dct = dict()
for i in range(1, max_val + 1):
    new_dct[i] = list()

for item in dct.items():
    new_dct[item[1]].append(item[0])

for item in new_dct.items():
    print(item)