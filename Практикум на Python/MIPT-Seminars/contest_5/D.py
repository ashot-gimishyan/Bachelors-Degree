import re

str_in = input()

while True:
    if len(set(str_in)) < 4:
        weak = True
        break

    if str_in == str_in.lower() or str_in == str_in.upper():
        weak = True
        break

    if re.search(r'ANNA', str_in.upper()) is not None:
        weak = True
        break

    if re.search(r'\d+', str_in) is None:
        weak = True
        break

    weak = False
    break

strong = not weak
print('weak' * weak + 'strong' * strong)

