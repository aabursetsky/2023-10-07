def print_params(a = 1, b = 'строка', c = True):
    print(a, b ,c)

print_params()                         # 1 строка True
print_params(b = 25)                   # 1 25 True
print_params(c = [1,2,3])              # 1 строка [1, 2, 3]
print_params((1, 's'), [True, False])  # (1, 's') [True, False] True

values_list = [['d', True], 75, (6, 66, 666)]
values_dict = {'a': 'Денис', 'b': 35, 'c': 'Казань'}

print_params(*values_list)              # ['d', True] 75 (6, 66, 666)
print_params(**values_dict)             # Денис 35 Казань

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)        # 54.32 Строка 42
