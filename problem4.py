#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"

import math
a = input("Enter a value for the side a: ")
a = float(a)

b = input("Enter a value for the side b: ")
b = float(b)

c = input("Enter a value for the side c: ")
c = float(c)

x = a**2
y = b**2
z = c**2

w = x + y

d = math.sqrt(x + y)
e = d * 0.02
f = d
d = d + e
f = d - e

if c >= f <= d:
  print("that is a right triangle")

elif w > z:
  print("that is an obtuse triangle")
  
elif w < z:
  print("that is an acute triangle")