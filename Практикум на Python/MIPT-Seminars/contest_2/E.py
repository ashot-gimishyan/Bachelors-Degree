input_str = input()
ls = input_str.split()
decimal = int(ls[0])
base = int(ls[1])
result = ""

while decimal:
    a = decimal % base
    result += str(a)
    a = int(a)
    decimal //= base
print(result[::-1])

