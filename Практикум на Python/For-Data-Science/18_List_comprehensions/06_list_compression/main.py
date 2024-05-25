N = [0,1,0,4,5,6,0,1,-1,10,11,0,0,0,5,6,7]

l = len(N)
for i in N:
    if i == 0:
        N.remove(i)

m = len(N)
for i in range(l - m + 1):
    N.append(0)

N = N[:m]
print(N)