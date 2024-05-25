mes = input()

res = str()
word = str()
for sym in mes:
    if sym.isalpha():
        word += sym
    else:
        word = word[::-1]
        res += word
        res += sym
        word = ""

print(res)