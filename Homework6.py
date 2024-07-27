mu_dict = {'Roman': 2006, 'Dima': 1893}
print(mu_dict['Dima'])
mu_dict['John'] = 2004
mu_dict.update({'Olga': 1344,
                'Misha': 2001})
del mu_dict['Olga']
print(mu_dict)
print(mu_dict.items())

my_set = {1, 1, 2, 3, 3, 3, 'Bread'}
print(my_set.add(75))
print(my_set.remove(2))
print(my_set)
