tup = (1,2,3,'sd')

def sort_tuple(t):
    def are_numbers(t):
        for i in t:
            if isinstance(t[i], int) == False:
                return False
        return True

    if are_numbers(t) is False:
        return t
    return tuple(sorted(list(t)))

print(sort_tuple(tup))