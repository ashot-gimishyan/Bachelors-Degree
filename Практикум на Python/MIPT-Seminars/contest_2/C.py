input_str = input()
ls = input_str.split()
N = int(ls[0])
M = int(ls[1])

for i in range(1, N+1):
    for j in range(1, M+1):
        print(i*j, end=" ")
    print('\n')

