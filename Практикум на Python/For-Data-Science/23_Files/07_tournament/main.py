K = None

count = 0
members = 0
file_1 = open('first_tour.txt', 'r')
file_2 = open('second_tour.txt', 'w')

members_list = list()

for line in file_1:
    count += 1
    if count == 1:
        K = int(line)

    else:
        line = line.split()
        if int(line[-1]) <= K:
            continue
        new_line = line[1][0] + ". " + line[0] + " " + line[2] + "\n"

        if len(members_list) == 0:
            members_list.append(new_line)
            continue

        for i in range(len(members_list)):
            tmp = members_list[i].split()
            if int(tmp[2]) < int(line[2]):
                members_list.insert(i, new_line)
                break

count = 0
file_2.write(str(len(members_list)) + '\n')
for data in members_list:
    count += 1
    file_2.write(str(count) + ") " + data)

