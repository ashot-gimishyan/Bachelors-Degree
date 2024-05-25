string = input()
words_list = list(string.split(' '))
words_dict = {}
for word in words_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
print(max(words_dict.values()) / len(words_list))

