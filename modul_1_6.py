my_dict = {'Дмитрий': 1977, 'Светлана': 1953}
print('my_dict:', my_dict)
print('Existing value:', my_dict['Дмитрий'])
print('Not existing value:', my_dict.get('Игорь'))
my_dict.update({'Владимир': 2000, 'Илья': 2013})
# print(my_dict)
print('Deleted value:', my_dict.pop('Владимир'))
print('Modified dictionary:', my_dict)

my_set = {1, 2, 2, 1, 'Portalle'}
print('Set:', my_set)
my_set.update( 'A')
my_set.discard(2)
print('Modified set:', my_set)