no = 'Пароль ненадёжный. Попробуйте ещё раз.'
yes = 'Это надёжный пароль!'

while True:
    password = input()
    if len(password) < 8:
        print(no)
    elif password.lower() == password:
        print(no)
    elif sum(s.isdigit() for s in password) < 3:
        print(no)
    else:
        print(yes)
        break
