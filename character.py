# Character Input
# Aeriel Denmark
# Wed 11/20/19

# www.practicepython.org

import math

name = input("What is your name?  ")
age = int(input("How old are you?  "))
year = int(input("What year is it?  "))
print("Year:  ", year)

print("Name:  ", name)
print("Age:  ", age)

def future(myParam):
	for i in age:
		future(year + 100)


# Sample Solution

# name = input("What is your name: ")
# age = int(input("How old are you: "))
# year = str((2014 - age)+100)
# print(name + " will be 100 years old in the year " + year)

