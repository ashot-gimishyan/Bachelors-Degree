def caesar_cipher(string, shift, alphabet):
    shift %= len(alphabet)
    coded_alphabet = alphabet[shift:] + alphabet[:shift]
    return ''.join([coded_alphabet[alphabet.find(letter)] if letter in alphabet else letter for letter in string])


file_1 = open('text.txt', 'r', encoding='utf-8')
file_2 = open('cipher_text.txt', 'w', encoding='utf-8')

eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0
for line in file_1:
    count += 1
    file_2.write(caesar_cipher(line, count, eng))

file_1.close()
file_2.close()
