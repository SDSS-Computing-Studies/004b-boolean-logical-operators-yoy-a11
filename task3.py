#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
import math
number = input()
n = False
f = False
integer_part = round(float(number))
if number[0] == '-':
    n = True
if float(number) - integer_part != 0:
    f = True
if not n and  not f:
    print(str(number) + " is a positive integer.")
else:
    print(str(number) + " is not a positive integer.")