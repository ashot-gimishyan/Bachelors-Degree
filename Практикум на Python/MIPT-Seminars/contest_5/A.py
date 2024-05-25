N = input()
N = int(N)

parts = []
parts.append('   _~_   ')
parts.append('  (o o)  ')
parts.append(' /  V  \\ ')
parts.append('/(  _  )\\')
parts.append('  ^^ ^^  ')

for part in parts:
    print(N * (part + ' '))

