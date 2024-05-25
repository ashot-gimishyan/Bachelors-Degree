while True:
    try:
        str_in = input().split('\t')
        length = 73 - len(str_in[4])
        str_out = str_in[0][0:7] + length * '.' + str_in[4]
        print(str_out)
    except EOFError:
        break

