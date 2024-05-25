def return_tuple(t, n):
    if n not in t:
        return tuple()
    start_index = 0
    stop_index = len(t) - 1

    for i in range(len(t)):
        if t[i] == n:
            start_index = i
            break

    for i in range(len(t) - 1, -1, -1):
        if t[i] == n:
            stop_index = i
            break

    return t[start_index:stop_index+1]

cortezh = (1,2,3,4,5,6, 3, 1)
print(return_tuple(cortezh, int(input()))) # на входе 3