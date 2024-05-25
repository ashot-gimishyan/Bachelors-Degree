a = input()
n = 2
_dict = {}

for i in range(len(a)):
    _dict[a[i]] = 1

i = 0
while i < len(a):
    if a[i: i+n] == a[i] * n:
        if _dict[a[i]] < n:
            _dict[a[i]] = n
        n += 1
    elif n > 2:
        i += n - 1
        n = 2
    elif n == 2:
        i += 1

for s in sorted(_dict.items()):
    print(s[0], s[1])

