def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c = [1,2,3])

values_list_ = [True, 54.32, 'Строка']
values_dict = {'a': 5, 'b': True, 'c': 5.3}

print_params(*values_list_)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)