N = int(input())
K = int(input())

display = ['I'] * N

for i in range(K):
    l, r = [int(s) for s in input().split()]
    display[l-1:r-1] = ['.'] * (r-l+1)
    display.pop(r)

print(''.join(display))