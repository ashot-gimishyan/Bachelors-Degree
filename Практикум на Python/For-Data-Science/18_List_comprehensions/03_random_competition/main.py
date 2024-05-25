import random

frst = [round(random.uniform(5, 10), 2) for _ in range(20)]
secd = [round(random.uniform(5, 10), 2) for _ in range(20)]
final = [(frst[i] if frst[i] > secd[i] else secd[i]) for i in range(20)]

print(frst)
print(secd)
print(final)