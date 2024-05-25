string = input()

gtr = 0
while gtr < len(string) - 1:
    if string[gtr:len(string) - 1] == string[len(string)-1:gtr:-1]:
        break
    gtr += 1

gtl = 0
while gtl < len(string) - 1:
    if string[0:len(string) - 1 - gtl] == string[len(string)-1 - gtl:0:-1]:
        break
    gtl += 1

print(gtl if gtr > gtl else gtr)

