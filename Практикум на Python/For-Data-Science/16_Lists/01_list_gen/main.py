N = int(input())

odd_nums = []

for i in range(1, N+1):
    if i % 2 == 1:
        odd_nums.append(i)


print(odd_nums)