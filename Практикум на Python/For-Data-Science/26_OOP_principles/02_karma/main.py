import random


class Karma:
    def __init__(self):
        self.count = 500

    def one_day(self):
        self.count -= random.randint(1,7)

        if self.count <= 0:
            print("Выход...")

        try:
            if self.count == 10:
                e = random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
                raise BaseException(e)

        except BaseException:
            try:
                file = open('karma.log', 'a')
            except [FileExistsError, FileNotFoundError]:
                file = open('karma.log', 'w')

            file.write(e+'\n')
            file.close()


karma = Karma()

while True:
    karma.one_day()
    if karma.count <= 0:
        break
