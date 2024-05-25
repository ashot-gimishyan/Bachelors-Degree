def summa(n):
    s = 0
    while n:
        s += n % 10
        n //= 10

    return s

def count(n):
    c = 0
    while n:
        c += 1
        n //= 10

    return c


n = int(input())
print(summa(n))
print(count(n))
print(summa(n) - count(n))

