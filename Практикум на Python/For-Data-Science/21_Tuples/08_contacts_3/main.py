contacts = dict()

while True:
    action = int(input("Действие: 1 - добавить контакт, 2 - найти человека: "))
    if action == 1:
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        phone_number = input("Введите номер телефона: ")
        s_key = (surname, name)
        if s_key in contacts.keys():
            print("Этот человек уже есть в контактах")
        else:
            contacts[s_key] = phone_number

    if action == 2:
        surname = input("Введите фамилию: ")
        for key, val in contacts.items():
            if surname.endswith('а'):
                if surname[:len(surname)-1].lower() == key[0].lower() or surname.lower() == key[0].lower():
                    print(key[0], key[1], val)
            else:
                if surname.lower() == key[0].lower() or surname.lower() == key[0][:len(key[0])-1].lower():
                    print(key[0], key[1], val)