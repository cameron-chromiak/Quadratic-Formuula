#Cameron Chromiak
#Oct 24 2018
#Solves quadratic equation

import math

aValue = input("Input a ")
bValue = input("Input b ")
cValue = input("Input c ")

aValue = float(aValue)
bValue = float(bValue)
cValue = float(cValue)


disc = (bValue ** bValue)-4*aValue*cValue

if (disc < 0):
  print("No solution")
elif (disc == 0):
  ans = -bValue / (2*aValue)
  print(ans)
else:
  ans = -bValue, "+-", disc / (2*aValue)
  print(ans)
