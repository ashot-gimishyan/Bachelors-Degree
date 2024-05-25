s = input()
b = str()
s = s + '1'
c = s[0]
i = 0

for r in s:
    if c != r:
        b += c + str(i)
        c = r
        i = 0
    i += 1

print(b)
