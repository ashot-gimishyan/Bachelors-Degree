def height(man):
    if man not in family_tree:
        return 0
    else:
        return 1 + height(family_tree[man])


family_tree = {}
number = int(input('Введите количество человек: '))
for i in range(1, number):
    print(i, end='')
    child, parent = input(' пара: ').split()
    family_tree[child] = parent

heights = {}
for man in set(family_tree.keys()).union(set(family_tree.values())):
    heights[man] = height(man)

for key, value in sorted(heights.items()):
    print(key, value)