N = int(input())
nums = [(1 if n % 2 == 0 else n % 5) for n in range(N)]
print(nums)