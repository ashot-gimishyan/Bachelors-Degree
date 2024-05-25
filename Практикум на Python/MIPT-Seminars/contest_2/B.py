X = input()
a = [int(i) for i in X]
Y = X
current_val = int(X)

while sum(a[:3]) != sum(a[3:]):
    X = int(X)
    X += 1
    X = str(X)
    a = [int(i) for i in X]

a = [int(i) for i in Y]
while sum(a[:3]) != sum(a[3:]):
    Y = int(Y)
    Y -= 1
    Y = str(Y)
    a = [int(i) for i in Y]

X = int(X)
Y = int(Y)
print(X if (X-current_val) < (current_val-Y) else Y)
