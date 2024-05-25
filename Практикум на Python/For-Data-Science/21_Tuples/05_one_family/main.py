family = {
    ('Сидоров', 'Никита') : 35,
    ('Иванова', 'Анна') : 20,
    ('Сидорова', 'Алина') : 34,
    ('Сидоров', 'Павел') : 10,
    ('Иванов', 'Джон') : 90
}


search = input()
for human in family.items():
    if (human[0][0].upper()).startswith(search.upper()):
        print(*(human[0] + (human[1],)))