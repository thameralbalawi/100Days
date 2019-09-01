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

# Day 7

print("######## exercise 1 #########")

print("hello")
print('hello')

print("######## exercise 2 #########")
a="hello"
print(a)

print("######## exercise 3 #########")

a ="""Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua."""
print(a)

print("######## exercise 4 #########")

a="Hello World"
print (a[1])
b="Hello World"
print (b[2:5])

# Day 8
a = "Hello, World!"

print(a.strip()) # returns "Hello, world"
print(len (a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', 'world']

# Day 9
print("######## exercise 1 #########")
age = 27
txt = "My name is Thamer, I am {}"
print(txt.format(age))

print("######## exercise 2 #########")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

print("######## exercise 3 #########")
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity, itemno, price))

# Day 10
print("######## exercise 1 #########")
x = 5
y = 3
z = 15
print(x - y)
print(x + y)
print(x * y)
print(x ** y)
print(x % y)
print(x / y)
print(x // y)
print("######## exercise 2 #########")
x /= 3
y += 4
z %= 5
print(x)
print(y)
print(z)
print("######## exercise 3 #########")
print(x < y)
print(z > x)

# Day 11
print("######## exercise 1 #########")
x = 5
print(x > 3 or x < 4)

print("######## exercise 2 #########")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
print(x is not y)
print(x != y)
print("banana" in x)

# Day 12
sentence = "Please, I want {} sandwishes and {} donutes"
sentence = sentence.format(5, 7)
sentence = sentence.replace("a", "A")
sentence = sentence.replace("I", "We")
print(sentence)

# Day 13
print("######## exercise 1 #########")
numbers = [1, 2, 3, 4, 5]
print(numbers)

print("######## exercise 2 #########")
thislist = ["apple", "banana", "cherry"]
print(thislist)

print("######## exercise 3 #########")
thislist2 = ["apple", "banana", "cherry", 1, 2, 3]
print(thislist2)
print(thislist[2])

print("######## exercise 4 #########")
for x in thislist:
    print(x)

Mylist = [56, 85, 5, 12]
for Ml in Mylist:
    print(Ml)

print("######## exercise 5 #########")
thislist[1] = "blckcurrent"
print(thislist)

del thislist[0]
print(thislist)