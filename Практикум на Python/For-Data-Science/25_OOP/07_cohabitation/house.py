class House:

    def __init__(self):
        self.__nightstand = 0
        self.__fridge = 50

    def empty_fridge(self, food):
        if self.__fridge >= food:
            self.__fridge -= food
            return True
        return False

    def fill_fridge(self, food):
        self.__fridge += food

    def empty_nightstand(self, money):
        if self.__nightstand >= money:
            self.__nightstand -= money
            return True
        return False

    def fill_nightstand(self, money):
        self.__nightstand += money

    def get_money(self):
        return self.__nightstand

    def get_food(self):
        return self.__fridge