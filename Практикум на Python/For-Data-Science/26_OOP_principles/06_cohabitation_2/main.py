class House:
    def __init__(self):
        self.money = 100
        self.refrigerator = 50
        self.cat_food = 30
        self.dirt = 0

    def __str__(self):
        return 'Денег {}, Еды в холодильнике {}, Корма для кота {}, Грязи {}'.format(
            self.money, self.refrigerator, self.cat_food, self.dirt)


class Human:
    def __init__(self, name, house):
        self.name = name
        self.degree_satiety = 30  # степень сытости
        self.degree_happy = 100  # степень счастья
        self.house = house

    def __str__(self):
        return 'Имя {}, Сытость {}, счастье {}'.format(
            self.name, self.degree_satiety, self.degree_happy)

    def eat(self):
        self.degree_satiety += 20
        self.house.refrigerator -= 20

    def petting_cat(self):
        self.degree_happy += 5
        self.degree_satiety -= 10


class Husband(Human):
    def __init__(self, name, house):
        super().__init__(name, house)

    def condition(self):
        if self.degree_happy < 10:
            print('Умер от депрессии')
        if self.degree_satiety <= 0:
            print('Умер от голода')
        if self.degree_satiety < 30:
            self.eat()
        if self.house.dirt > 90:
            self.degree_happy -= 10
        self.house.dirt += 5
        if self.house.money < 1000:
            self.work()
        if self.degree_happy < 20:
            self.play()
            self.petting_cat()

    def play(self):
        self.degree_satiety -= 10
        self.degree_happy += 20

    def work(self):
        self.degree_satiety -= 10
        self.house.money += 150


class Wife(Human):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.coat_count = 0
        self.buy_food_count = 0

    def condition(self):
        if self.degree_happy < 10:
            print('Умер от депрессии')
        if self.degree_satiety <= 0:
            print('Умер от голода')
        if self.degree_satiety < 30:
            self.eat()
        if self.house.dirt > 90:
            self.degree_happy -= 10
            self.clean_house()
        self.house.dirt += 5
        if self.degree_happy < 20:
            self.buy_coat()
            self.petting_cat()
        if self.house.refrigerator < 20 or self.house.cat_food < 20:
            self.buy_food()

    def buy_food(self):
        self.degree_satiety -= 10
        self.house.refrigerator += 30
        self.house.cat_food += 10
        self.house.money -= 30
        self.buy_food_count += 30

    def buy_coat(self):
        self.degree_satiety -= 10
        self.house.money -= 350
        self.degree_happy += 60
        self.coat_count += 1

    def clean_house(self):
        self.degree_satiety -= 10
        self.house.dirt -= 100


class Cat:
    def __init__(self, name, house):
        self.name = name
        self.degree_satiety = 30
        self.house = house

    def __str__(self):
        return 'Имя {}, Сытость {}'.format(self.name, self.degree_satiety)

    def condition(self):
        if self.degree_satiety <= 0:
            print('Умер от голода')
        if self.degree_satiety < 25:
            self.eat()
        else:
            self.sleep()
            self.wallpaper()

    def eat(self):
        self.degree_satiety += 10 * 2
        self.house.cat_food -= 5

    def sleep(self):
        self.degree_satiety -= 10

    def wallpaper(self):
        self.degree_satiety -= 10
        self.house.dirt += 5


my_house = House()
human = Human(name='Vova', house=my_house)
husband = Husband(name='Vova', house=my_house)
wife = Wife(name='Vika', house=my_house)
cat = Cat(name='Murka', house=my_house)


for day in range(1, 366):
    print('\nДень {}:'.format(day))
    print('Муж:', husband)
    print('Жена:', wife)
    print('Дом:', my_house)
    print('Кот:', cat)
    wife.condition()
    husband.condition()
    cat.condition()

print('\nЗаработано денег: ', my_house.money)
print('Куплено еды: ', wife.buy_food_count)
print('Куплено шуб: ', wife.coat_count)
