#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
import math
import cmath

print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")
#convert to a number
a=input("Emter a number: ")
#convert to a number
a=float(a)
b=input("Enter a number: ")
#convert to a number
b=float(b)
c=input("Enter a number: ")
#convert to a number
c=float(c)

x1 = (math.sqrt((pow(b,2)-4*a*c))-b) / (2*a)
x1=float(x1)
x2 = (- 1*math.sqrt((pow(b,2)-4*a*c))-b)/(2*a)
x2=float(x2)
try:
  if x1== isnumeric(x1) and x2 == isnumeric(x2):  
    print(x1,x2)

except:
  print("Those are not valid values for a, b or c")
