#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
# hi
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

import math

a = int(input("enter side a\n"))
b = int(input("enter side b\n"))
x = math.sqrt((a ** 2) + (b ** 2))
print(x)