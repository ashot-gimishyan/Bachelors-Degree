f_str = input()
s_str = input()
my_dict = dict(zip(f_str, s_str))
f_len = len(f_str)
s_len = len(s_str)
for i in range(0, f_len - s_len):
    my_dict[f_str[i + s_len]] = None
print(sorted(list(my_dict.items())))

