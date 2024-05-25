ip = input().split('.')

if len(ip) != 4:
    print('Адрес - это четыре числа, разделенные точками')
elif not ip[-1].isdigit():
    print(ip[-1], "- не целое число")
elif int(ip[-1]) > 255:
    print(ip[-1], "превышает 255")
else:
    print('IP-адрес корректен')