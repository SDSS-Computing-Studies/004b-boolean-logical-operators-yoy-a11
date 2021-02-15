#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = min(a,b)
d = max(a,b)
if d % c == 0:
    print(str(c) + " is a factor of " + str(d))
else:
    print(str(c) + " is not a factor of " + str(d))