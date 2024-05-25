import math


class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = math.radians(angle)

    def move(self, distance):
        self.x = round(self.x + distance * math.cos(self.angle), 2)
        self.y = round(self.y + distance * math.sin(self.angle), 2)


class Bus(Car):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.passenger = 0
        self.money = 0
        self.peoples = 0

    def move(self, distance):
        super().move(distance)
        self.money += self.peoples * distance

    def put(self, passenger):
        self.passenger += passenger
        self.peoples += passenger
        print(f'Зашли {passenger} пассажира(ов)')

    def push(self, passenger):
        self.passenger -= passenger
        print(f'Вышли {passenger} пассажира(ов)')


bus = Bus(x=0, y=0, angle=60)
bus.put(10)
bus.push(3)
bus.move(distance=10)
print(f'Остались {bus.passenger} пассажира(ов)')
print(f'Транспортная компания заработала: {bus.money}')
print(f'Координаты: {bus.x}, {bus.y}\n')

Bus(bus.x, bus.y, angle=86)
bus.put(25)
bus.push(27)
bus.move(distance=25)
print(f'Остались {bus.passenger} пассажира(ов)')
print(f'Транспортная компания заработала: {bus.money}')
print(f'Координаты: {bus.x}, {bus.y}')
