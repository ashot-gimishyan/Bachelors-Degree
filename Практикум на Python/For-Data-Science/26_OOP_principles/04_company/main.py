class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return 'Имя: {}. Фамилия: {}. Возраст: {}. '.format(
            self.__name, self.__surname, self.__age)


class Employee(Person):
    pass

    def get_salary(self):
        salary = 0
        return salary


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def get_salary(self):
        salary = 13000
        return f'Заработная плата: {salary}\n'


class Agent(Employee):
    def __init__(self, volume, name, surname, age):
        super().__init__(name, surname, age)
        self.volume = volume

    def get_salary(self):
        salary = 5000 + 0.05 * self.volume
        return f'Заработная плата: {salary}\n'


class Worker(Employee):
    def __init__(self, hours, name, surname, age):
        super().__init__(name, surname, age)
        self.hours = hours

    def get_salary(self):
        salary = 100 * self.hours
        return f'Заработная плата: {salary}\n'


first_manager = Manager(name='John', surname='Mcafee', age=15)
second_manager = Manager(name='Bill', surname='Gates', age=51)
third_manager = Manager(name='John', surname='Connor', age=25)
print(first_manager, first_manager.get_salary())

first_agent = Agent(name='Bill', surname='Gates', age=16, volume=168500)
second_agent = Agent(name='John', surname='Mcafee', age=52, volume=158500)
third_agent = Agent(name='John', surname='Connor', age=26, volume=128500)
print(first_agent, first_agent.get_salary())

first_worker = Worker(name='John', surname='Connor', age=17, hours=168)
second_worker = Worker(name='Bill', surname='Gates', age=53, hours=170)
third_worker = Worker(name='John', surname='Mcafee', age=27, hours=192)
print(first_worker, first_worker.get_salary())
