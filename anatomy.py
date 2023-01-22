# !/usr/bin/python
# This is a python module
# lines one and two are just comments
import sys
# pythons user system module sys is a sytem
argument_count = len(sys.argv)
# argv is an argument vector- vector = a list so in this case a list of arguments
# argument = an input (something we pass into something)
# if a microwave was a function the argument would be the food you put in, the time, the power
print(argument_count)
# argc is our variable
# sys.argv - these count the number of arguments (items) passed to the command line
# argc is a variable and len is a function which means the number of items. Right associative
# length is a building function which calculates the length of whatever you have inside
if argument_count > 0:
    # a conditional
    print ('Too many inputs')
    # if the variable has  a value greater than one (in this case the number of items)
else:
    where = 'World' # create a variable where and assign the value 'World' to it
#     print("Hello", where) #takes multiple arguments / parameters/ inputs
#     print ('one', 'two', 'three')
# print ('Goodbye from ' + sys.argv[0])
# Square brackets are a list

platform = sys.platform

print(platform)



