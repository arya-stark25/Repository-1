# Importing Modules
# Use a generic import to import "random" module.
# Use a universal import toget everything from the "math" module.
# Use a function import to get exit() function from the "sys" module.
# Use a function from the random module to generate a float greater than or equal to 0 and less than 100 and assign that number to a variable.
# Use a sqrt() function from the math module to get the square root of the number from the step4 and assign that to a variable.
# Call the exit() function from the sys module with the variable from the step 5 as what it will display.

import random
from math import*
from sys import exit
A= random.uniform(0,100)
print("The Generated floating point number is", A)
SR= sqrt(A)
print("The Square root", SR)
#exit(SR)









