class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def about(self):
        print(f"Я - {self.name}\nМой возраст: {self.age}\nМои дети: ", end='')
        print(self.children, sep=' ')

    # Успокоить ребёнка
    def soothe_child(self, name):
        for child in self.children:
            if child.name == name:
                child.is_quiet = True
                break
        else:
            print(f'{name} не мой ребенок...')

    # Покормить ребёнка
    def feed_child(self, name):
        for child in self.children:
            if child.name == name:
                child.is_hungry = False
                break
        else:
            print(f'{name} не мой ребенок...')

class Child:

    def __init__(self, name, age, is_hungry, is_quiet):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
        self.is_quiet = is_quiet


doughter = Child('Анна', 2, False, False)
son = Child('Дима', 10, True, False)
parent = Parent("Иван", 35, [doughter, son])

print(son.is_hungry)
parent.feed_child(son.name)
print(son.is_hungry)

print(doughter.is_quiet)
parent.soothe_child(doughter.name)
print(doughter.is_quiet)

parent.soothe_child('Барак Обама')

