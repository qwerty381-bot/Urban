def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(1)
print_params(1, 'строка')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1, '(-_-)', False]
values_dict = {'a': 'NGG', 'b': 52, 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'str']
print_params(*values_list_2, 42)
