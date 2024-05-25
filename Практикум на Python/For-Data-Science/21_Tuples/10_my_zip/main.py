def my_zip(s, t):
    min_len = min(len(s), len(t))

    for i in range(min_len):
        yield s[i], t[i]

s = "abcd"
t = (10, 20, 30, 40)

for pair in my_zip(s,t):
    print(pair)

