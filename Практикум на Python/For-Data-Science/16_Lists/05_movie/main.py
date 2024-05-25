films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

your_film = input()

favourite_films = []
if your_film in films:
    favourite_films.append(your_film)
else:
    print("error")

print(*favourite_films)
