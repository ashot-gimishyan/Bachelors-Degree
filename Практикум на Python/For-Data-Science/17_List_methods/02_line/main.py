
first = []
for i in range(160, 176, 2):
    first.append(i)

second = []
for i in range(162, 180, 3):
    second.append(i)

first.extend(second)
print(sorted(first, reverse=False))
