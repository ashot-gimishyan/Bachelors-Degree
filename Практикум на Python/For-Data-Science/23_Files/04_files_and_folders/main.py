import os


def info(new_path):
    total_size, dir_count, file_count = 0, 0, 0

    for dir_path, dir_names, file_names in os.walk(new_path):
        dir_count += len(dir_names)
        file_count += len(file_names)

        for file in file_names:
            new_path = os.path.join(dir_path, file)
            total_size += os.path.getsize(new_path)

    total_size = round((total_size / 1024), 2)

    print('Размер каталога (в Кб): ', total_size)
    print('Количество подкаталогов: ', dir_count)
    print('Количество файлов: ', file_count)


path = input('Введите путь до каталога: ')
info(path)
