#!/usr/bin/python3

my_dict = {'age': 29, 'status': 'single', 'hometown': 'Daura', 'name': 'Murtala', 'career': 'SE'}
print(my_dict)

print(my_dict['status'])
print(my_dict['age'])
print(my_dict['hometown'])

my_dict['hometown'] = 'Oyo'
print(my_dict['hometown'])

my_dict['name'] = 'Mudi'
print(my_dict['name'])
print(my_dict)

my_dict['goal'] = 'integrity'
print(my_dict)

del my_dict['age']
print(my_dict)