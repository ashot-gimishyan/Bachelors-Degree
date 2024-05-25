string = input().split()

max_len = 0
max_word = ""

for word in string:
    if len(word) > len(max_word):
        max_word = word

print(max_word, len(max_word))