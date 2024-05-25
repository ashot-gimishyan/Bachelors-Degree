players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

lst = list()
for item in players.items():
    lst.append(item[0] + item[1])
print(lst)
