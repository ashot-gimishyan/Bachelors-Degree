from math import ceil

def is_prime(numbers):
    return [True if i % ceil((i / 2)) != 0 else False for i in numbers]


data = [3, 5, 7, 11, 12, 13, 14, 15, 16, 17]

print(is_prime(data))

for i in data:
    for j in is_prime(data):
        if not j:
            if i in data:
                data.remove(i)

print(data)
