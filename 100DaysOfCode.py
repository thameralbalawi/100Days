import random

# Day 1
print("Hello, World!")
if 5 > 2:
    print("Five is greater than two!")

# Day 2
"""
this is a comment 
written in 
more than just one line
"""

# Day 3
######## exercise 1 #########
x = 4 # x is of type int
x = "Sally"  # x is now of type str
print(x)
######## exercise 2 #########
x = "Python is "
y = "awesome"
z = x + y
print(z)

# Day 4
x = 1 # int
y = 208 #float
z = 1j # complex

#conver from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Day 5
x = "apple"
y = "orange"
z = "limon"

basket = [x , y , z]
n= [5]
[basket[sum(n[:i]):sum(n[:i+1])] for i in range(len(n))]