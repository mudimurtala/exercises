#!/usr/bin/python3

# asking the user to type the present year
present_year = int(input('Enter the current year you are in right now: '))

# asking the user to type his/her birth year
birth_year = int(input('Type in your birth year: '))

# let's now calculate the age of the user
age = present_year - birth_year

# let's display the user's age
print('Your age is:', age)