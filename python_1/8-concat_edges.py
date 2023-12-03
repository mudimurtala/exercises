#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:-63] + str[106:112] + str[0:6]
# str = ''.join(str[39:-63]) + " " + "with Python"
# print(str[str.find("object-oriented programming"):].split()[0] + " " + str.split()[-1])

print(str)

import this