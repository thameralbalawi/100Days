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
print("######## exercise 1 #########")
x = 4 # x is of type int
x = "Sally"  # x is now of type str
print(x)
print("######## exercise 2 #########")
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

import random
print(random.randrange(1,10))

# Day 5
x = "apple"
y = "orange"
z = "limon"

basket = [x , y , z]
n= [5]
[basket[sum(n[:i]):sum(n[:i+1])] for i in range(len(n))]

# Day 6
print("######## exercise 1 #########")
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
print("######## exercise 2 #########")
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
print("######## exercise 3 #########")
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)