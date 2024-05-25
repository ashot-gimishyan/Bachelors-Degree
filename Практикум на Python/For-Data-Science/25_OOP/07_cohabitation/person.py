from house import House


def get_person_count():
    return Person.__count


class Person:
    __count = 0

    def __init__(self, name, house):
        self.__fullness = 50
        self.__fullness_spend_step = 1
        self.__fullness_earn_step = 1
        self.__money_spend_step = 1
        self.__money_earn_step = 1
        self.__fridge_empty_step = 1
        self.__fridge_fill_step = 1
        self.set_name(name)
        self.move_in(house)
        Person.__count += 1

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception('Incorrect name. Must be string value.')

    def move_in(self, house):
        if isinstance(house, House):
            self.__house = house
        else:
            raise Exception('Error! Expected House_Object as an attribute.')

    def spend_fullness(self):
        self.__fullness -= self.__fullness_spend_step

    def earn_fullness(self):
        self.__fullness += self.__fullness_earn_step

    def spend_money(self):
        return self.__house.empty_nightstand(
            self.__money_spend_step
        )

    def earn_money(self):
        self.__house.fill_nightstand(
            self.__money_earn_step
        )

    def spend_food(self):
        if self.__house.empty_fridge(self.__fridge_empty_step):
            print('+1 to fullness \U0001F643')
            return True
        else:
            print('Failed to eat \U0001F615')
            return False

    def earn_food(self):
        self.__house.fill_fridge(self.__fridge_fill_step)

    def eat(self):
        if self.spend_food():
            self.earn_fullness()

    def work(self):
        self.spend_fullness()
        self.earn_money()
        print('Worked \U0001F610')

    def play(self):
        self.spend_fullness()
        print('Good mood after play \U0001F601')

    def go_shopping(self):
        if self.spend_money():
            self.earn_food()
            print('Earn some food \U0001F60E')
        else:
            print('Not enough money \U0001F614')

    def get_name(self):
        return self.__name

    def get_fullness(self):
        return self.__fullness

    def __str__(self):
        return '{}: fullness: {}, money: {}, food: {}'.format(
            self.get_name(),
            str(self.get_fullness()),
            str(self.__house.get_money()),
            str(self.__house.get_food())
        )

    def is_alive(self):
        if self.__fullness >= 0:
            return True
        return False