def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a='LOVE')
print_params(c=False, a=(357, 678, 789))  #в а должен вывестись кортеж
print_params(b=25, c=[1, 2, 3])  #в с список

values_list = ([1, 2, 3], True, 'string')
values_dict = {'a': True, 'b': 'love', 'c': 12}
print_params(*values_list)
print_params(**values_dict)

values_list2 = ([1, 2, 3], 'string')
print_params(*values_list2, 42)


