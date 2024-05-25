first = []
for i in range(3):
    first.append(int(input()))

second = []
for i in range(7):
    second.append(int(input()))

first.extend(second)
print(list(set(first)))
