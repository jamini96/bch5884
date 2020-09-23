#!/usr/bin/env python3

#https://github.com/jamini96/bch5884me.git

#Find the angles of a triangle

import math

# Enter the values for each side of the triangle

A = float(input("Enter the length of side A:"))
B = float(input("Enter the length of side B:"))
C = float(input("Enter the length of side C:"))

a =math.degrees(math.acos((((A**2)+(C**2)-(B**2))/(2*A*C))))
print("The angle of a is ", a)
b =math.degrees(math.acos((((A**2)+(B**2)-(C**2))/(2*A*B))))
print ("The angle of b is ", b)
c =math.degrees(math.acos((((B**2)+(C**2)-(A**2))/(2*B*C))))
print ("The angle of c is ", c)
