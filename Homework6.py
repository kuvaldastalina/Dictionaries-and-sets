mu_dict = {'Roman': 2006, 'Dima': 1893}
mu_dict['John'] = 2004
mu_dict.update({'Olga': 1344, 'Misha': 2001})
print(mu_dict)

print(mu_dict['Dima'])
print(mu_dict.get('Egor'))


a = mu_dict.pop('Olga')
print(mu_dict)
print(a)

print(mu_dict.items())

my_set = {1, 1, 2, 3, 3, 3, 'Bread'}
print(my_set.add(6))
print(my_set.add(7))
print(my_set.remove(2))
print(my_set)
)
