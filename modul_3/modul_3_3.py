def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=1225)
print_params(c=[1, 2, 3])
values_list = [12, False, 'Urban']
values_dict = {'a': '2024', 'b': True, 'c': 15.01}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [44, 'String']
print_params(*values_list_2, 42)
