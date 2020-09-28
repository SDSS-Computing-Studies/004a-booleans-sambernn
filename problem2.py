#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

import math
print("enter a number")
x = input()
x = float(x)
x2 = math.floor(x)
if x == x2:
    print('the number is an integer')
else:
    print('the number is not an integer')
