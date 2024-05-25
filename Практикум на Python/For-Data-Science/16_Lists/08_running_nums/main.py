s = int(input())

lst = input().split(' ')
lst = [int(num) for num in lst]

print(lst)

for _ in range(s):
    lst = lst[-1:] + lst[:-1]

print(lst)