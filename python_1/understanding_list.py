#!/usr/bin/python3

# manipulating a list in python

mudi_list = [1, 3, 60, "mango", 'banana', 56.45, 'table', 23]
# print(mudi_list)

fruits = ['apple', 'orange', 'banana']
# print(fruits)

siblings = ['amoke', 'amope', 'adunni']
# print(siblings)


fruits[1] = 'ogede'
fruits.append('oronbo')
# print(fruits)
removed_fruits = fruits.pop(3)
# print(fruits)
# print(removed_fruits)
fruits.insert(1,'oronbo')
# print(fruits)
# print(len(fruits))
# print(fruits[-3])


siblings[1] = 'ishola'
siblings.append('ayinde')
siblings.append('abiodun')
# print(siblings)

square = [x**4 for x in range(1, 11)]
# print(square)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)
odd_numbers = [x for x in numbers if x % 2 == 1]
# print(odd_numbers)

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
# print(result_matrix)

mudis_set = {3,5,9,8,39,28}
mudis_set.add(100)
mudis_set.remove(39)
# print(mudis_set)
mudis_two = [2,3,8,75,20,48,92]
# print(mudis_two)
# print(101 in mudis_set)

fruits2 = {'apple','banana','orange','grape','kiwi'}
fruits2.add('pear')
print(fruits2)