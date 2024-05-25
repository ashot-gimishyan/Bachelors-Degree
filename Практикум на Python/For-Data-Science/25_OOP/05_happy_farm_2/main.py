class Potato:

    states = {
        0: 'absent',
        1: 'sprout',
        2: 'unripe',
        3: 'ripe'
    }

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state <= 3:
            self.state += 1

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('_[{} is {}]_'
              .format(self.index, Potato.states[self.state]), end='')


class PotatoGarden:

    def __init__(self, count):
        self.count = count
        self.potatoes = [Potato(index) for index in range(count)]

    def grow_all(self):
        print('Potatoes are growing!')
        for potato in self.potatoes:
            potato.grow()

    def all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            return False
        else:
            return True

    def get_state(self):
        print('GARDEN: ', end='')
        for potato in self.potatoes:
            potato.print_state()

    def harvest_potatoes(self):
        if self.all_ripe():
            for potato in self.potatoes:
                potato.state = 0
            print('All potatoes harvested!')
            return self.count
        else:
            print('Potatoes are not ready to be harvested')
            return None


class Gardener:

    def __init__(self, name, garden):
        self.__harvest = []
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Error! "name" argument must be a string.')
        if isinstance(garden, PotatoGarden):
            self.garden = garden
        else:
            raise TypeError('Error! Expected PotatoGarden as an argument.')

    def tend(self):
        self.garden.grow_all()

    def harvest(self):
        result = self.garden.harvest_potatoes()
        if result is not None:
            self.__harvest.append(result)

    def get_harvest_info(self):
        print('Actual harvest: {}'.format(self.__harvest))


my_garden = PotatoGarden(count=5)
me = Gardener(name='Bob', garden=my_garden)

for i in range(3):
    print('\n')
    print('Day {} has come!'.format(i + 1))
    my_garden.get_state()
    me.tend()
    me.harvest()
    me.get_harvest_info()

print('\n')
my_garden.get_state()