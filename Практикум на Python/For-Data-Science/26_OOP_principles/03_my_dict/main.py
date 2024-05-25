class MyDict:
    data = {'a': 9}

    def __init__(self, key):
        self.key = key

    def get_value(self):
        value = self.data.get(self.key, 0)
        return value


my_key = input('Введите ключ: ')
search = MyDict(my_key)
search_key = search.get_value()
print(search_key)
