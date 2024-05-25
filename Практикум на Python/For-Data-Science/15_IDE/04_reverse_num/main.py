def rev(num):
    return num[::-1]

n1 = input()
n2 = input()

n1 = n1.split('.')
n2 = n2.split('.')

print(rev(n1[0]) + '.' + rev(n1[1]))
print(rev(n2[0]) + '.' + rev(n2[1]))
print(float(rev(n1[0]) + '.' + rev(n1[1])) + float(rev(n2[0]) + '.' + rev(n2[1])))