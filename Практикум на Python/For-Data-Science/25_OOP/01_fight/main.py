import random
class A:
    def __init__(self, health):
        self.health = health

    def display_health(self):
        print("Я первый. Количество моих очков: {}".format(self.health))

class B:
    def __init__(self, health):
        self.health = health

    def display_health(self):
        print("Я второй. Количество моих очков: {}".format(self.health))


first = A(100)
second = B(100)

random.seed()
lst = [first, second]
while first.health > 0 and second.health > 0:
    atacker = random.choice(lst)
    if atacker is first:
        second.health -= 2
        print(f"Атаковал первый, у второго {second.health} очков")
    else:
        first.health -= 2
        print(f"Атаковал второй, у первого {first.health} очков")

if first.health:
    print("Победил первый")
else:
    print("Победил второй")