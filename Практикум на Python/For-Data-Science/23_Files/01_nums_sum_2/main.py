# TODO здесь писать код

file = open('numbers.txt', 'r')

sum = 0
for line in file:
    if line.strip() != '':
        sum += int(line.strip())
file.close()

file = open('answers.txt', 'w')
file.write(str(sum))
file.close()

# print(sum)

