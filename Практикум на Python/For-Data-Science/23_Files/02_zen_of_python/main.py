file = open('zen.txt', 'r')

zen_list = list()

for f in file:
    zen_list.append(f)
file.close()

zen_list = zen_list[::-1]
for line in zen_list:
    print(line, end="")