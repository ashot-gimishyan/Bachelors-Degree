from random import randint

def make_pairs(t):
    for i in range(len(t)-1):
        yield t[i], t[i+1]

numbers = [randint(1, 100) for _ in range(10)]
numbers = tuple(numbers)

j = 0
numbers_pairs = []
for pair in make_pairs(numbers):
    if j % 2 == 0:
        numbers_pairs.append(pair)
    j+=1

print(numbers_pairs)
