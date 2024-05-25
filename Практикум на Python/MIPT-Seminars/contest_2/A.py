n = int(input())
ls = []

for i in range(1, n+1):
    if not i % 15:
        ls.append("Fizz Buzz")
    elif not i % 5:
        ls.append("Buzz")
    elif not i % 3:
        ls.append("Fizz")
    else:
        ls.append(i)

print(*ls, sep=", ")

