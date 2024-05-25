from collections import Counter
string = input()
N = int(input())
sub = [string[i:i + N] for i in range(0, len(string) - N + 1)]
counted = Counter(sub)
print(sorted([sub for (sub, counted) in list(counted.items()) if counted > 1]))
