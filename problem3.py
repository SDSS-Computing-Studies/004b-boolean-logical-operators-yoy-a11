#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

a = int(input("please enter number a "))
b = int(input("please enter number b "))
c = int(input("please enter number c "))
Pythagorean triples = [a,b,c]
Pythagorean triples.sort()
print(Pythagorean triples)
sum_of_square = Pythagorean triples[0] ** 2 + Pythagorean triples[1] ** 2
single_square = Pythagorean triples[2] ** 2
if sum_of_square == single_square: 
    print("xx,yy,zz form a Pythagorean Triple")
else:
    print("xx,yy,zz do not form a Pythagorean Triple")

