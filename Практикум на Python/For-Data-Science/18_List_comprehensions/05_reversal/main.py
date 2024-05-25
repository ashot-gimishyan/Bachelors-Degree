string = input().split('h')
string.pop(-1)
string.pop(0)
string = 'h'.join(string)
string = string[::-1]
print(string) # между 1 и -1 h