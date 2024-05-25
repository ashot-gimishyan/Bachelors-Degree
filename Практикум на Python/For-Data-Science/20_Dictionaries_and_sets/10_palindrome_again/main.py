import itertools

def is_palindrom(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

word = list(input())
permutations = list(itertools.permutations(word))
permutations_set = set([''.join(permutation) for permutation in permutations])

for permutation in permutations_set:
    if is_palindrom(permutation):
        print("Можно сделать палиндромом")
        break
else:
    print("Нельзя сделать палиндромом")