word = input()

flag = True
for i in range(len(word)//2):
    if word[i] != word[len(word)-i-1]:
        flag = False

if flag is True:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')