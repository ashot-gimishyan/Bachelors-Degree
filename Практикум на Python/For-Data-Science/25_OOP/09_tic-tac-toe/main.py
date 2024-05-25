win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

class Field:
    field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        self.__init_board()

    def __init_board(self):
        print('-' * 13)
        for i in range(3):
            print('|', self.field[0 + i * 3], '|', self.field[1 + i * 3], '|', self.field[2 + i * 3], '|')
            print('-' * 13)

    def Draw(self, sing):
        while True:
            index = (input('\nКуда поставить {}:  '.format(sing)))
            if index not in self.field:
                print('Выберите свободную клетку на поле!')
            else:
                self.field[int(index) - 1] = sing
                self.__init_board()
                break

    def Check(self, comb):
        for (x, y, z) in comb:
            if self.field[x - 1] == self.field[y - 1] and self.field[y - 1] == self.field[z - 1]:
                return True
        else:
            return False

    def Select(self):
        choice = input('Кто ходит первый? Х/О \n').lower()
        while choice != 'x' and choice != 'o':
            print('Введите Х или О!')
            choice = input('Кто ходит первый? Х/О \n').lower()
        return True if choice == 'x' else False

    def Play(self):
        if self.Select():
            while True:
                self.Draw('X')
                if self.Check(win):
                    print('X выиграл')
                    break
                self.Draw('O')
                if self.Check(win):
                    print('O выиграл')
                    break
        else:
            while True:
                self.Draw('O')
                if self.Check(win):
                    print('O выиграл')
                    break
                self.Draw('X')
                if self.Check(win):
                    print('X выиграл')
                    break


f = Field()
f.Play()