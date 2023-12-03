#!/usr/bin/python3

set1 = {1, 3, 5, 8}
set1.add(('home', 'abroad'))
set1.add('Messi')
set2 = {30,87}

set1.update(set2)
ourset = set(('Timi', 4.7, 'Weed', 5))
ourset.union(set1)
print(ourset)