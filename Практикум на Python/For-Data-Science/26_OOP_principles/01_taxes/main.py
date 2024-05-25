class Property:
    def __init__(self):
        pass
    def method(self, worth):
        pass
class Apartment(Property):
    def method(self):
        return 0.001 * self.worth
    def __init__(self, m):
        self.worth = m
class Car(Property):
    def method(self):
        return 0.005 * self.worth

    def __init__(self, m):
        self.worth = m

class CountryHouse(Property):
    def method(self):
        return 0.002 * self.worth

    def __init__(self, m):
        self.worth = m



# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества , а затем выдает ему налог на соответствующее имущество и сколько денег ему не хватает (если это так)

money = float(input("Сколько у вас денег? "))

car = Car(float(input("Стоимость машины: ")))
apart = Apartment(float(input("Стоимость квартиры: ")))
chouse = CountryHouse(float(input("Стоимость дачи: ")))

total = car.method() + apart.method() + chouse.method()

if total > money:
    print(f"Не хватает {total - money}")
else:
    print("OK")





