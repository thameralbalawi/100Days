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

# Day 14
thislist = ["A", "B", "C", "D", "E"]
print(thislist[1:3])

thislist2 = ["apple", "banana", "cherry"]
if "apple" in thislist2:
    print("yes, 'apple' is in the fruits list")
    
thislist = ["بايثون"] * 4
print(thislist)

thislist1 = ["Ahmad", "Khalid", "Omar"]
thislist2 = ["Sara", "Hind", "Batool"]
thislist3 = thislist1 + thislist2
print(thislist3)

number1 = [7.5, 3.6, 4.7]
number2 = [6, 4, 8]
number3 = number1 + number2
print(thislist3)

# Day 15
thislist3 = ["apple", "banana", "cherry"]
BackupList = thislist3.copy()
Backup2List = list(thislist3)
print(len(thislist3))
thislist3.append("orange")
print(thislist3)
thislist3.insert(1, "orange")
print(thislist3)
thislist3.pop(4)
print(thislist3)
thislist3.remove("orange")
print(thislist3)
thislist3.clear()
print(thislist3)
print(BackupList)
print(Backup2List)

# Day 16 
thistuple =("apple", "banana", "cherry")
print(thistuple)

thistuple=()
print(thistuple)

thistuple=(3.)
print(thistuple)

thistuple2 =(3, 1.3, 4.1, 7)
print(thistuple2)
print(thistuple2[0])
for x in thistuple2:
    print(x)

print("######## exercise 1 #########")
thistuple3 =("apple", "banana", "cherry")
for x in thislist3:
    print(x)

print("######## exercise 2 #########")
thistuple3 =("apple", "banana", "cherry", "orange")
print(thistuple3[0:3])

# Day 17
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("yes, 'apple' is in the fruts tuple")

    thistuple= ("بايثون",) * 3
    print(thistuple)

thistuple1 = (1, 2, 3, 4)
thistuple2 = (5, 6)

thistuple = thistuple1 + thistuple2
print(thistuple)

print("######## exercise 1 #########")
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print("######## exercise 2 #########")
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[1])
print(thistuple1[-2])
print(thistuple1[0:4])

# Day 18 - 19
print("######## exercise 1 #########")
tuple =["java", "python", "swift", "PHP", "C++"]
check_list = ["java", "python", "swift"]
tuple.append('R')
print(tuple)
tuple.insert(1,'kotlin')
print(tuple)
tuple.remove('swift')
print(tuple)
tuple.sort()
print(tuple)
tuple.pop()
print(tuple)

print("######## exercise 2 #########")
tuple =["java", "python", "swift", "PHP", "C++"]
if "java" in tuple:
    print("java is exist")
else:
 print("sorry, java not found in the list")

if "python" in tuple:
    print("python is exist")
else:
 print("sorry, python not found in the list")

if "swift" in tuple:
    print("swift is exist")
else:
 print("sorry, swift not found in the list")
 
if "C#" in tuple:
    print("C# is exist")
else:
 print("sorry, C# not found in the list")

# Day 20
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("apple" in thisset)
thisset.add("orange")
thisset.update(["orange","mango", "grapes"])
print(thisset)

# Day 21
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
x = thisset.pop()
print(x)
thisset.clear()
print(thisset)
del thisset

thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Day 22
thisdict1 = {}
print(thisdict1)

thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict2)

x = thisdict2["model"]

x = thisdict2.get("model")
print(x)

thisdict2["year"] = 2018
print(thisdict2)

for x in thisdict2:

    print(x)

for x in thisdict2:

    print(thisdict2[x])

for x in thisdict2.values():

    print(x)

for x, y in thisdict2.items():

    print(x, y)

# Day 23
thisdict = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
}

if "model" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict_2 dictionary ")

print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)


del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)


# Day_24

thisdict = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
}

copy_dict_1 = thisdict.copy()
print(copy_dict_1)

copy_dict_2 = dict(thisdict)
print(copy_dict_2)

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },

    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

thisdict1 = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict1)


# Day 25 - 26
set = {1, 3, 5, 7, 8}
set.update([4, 8, 12])
print(set)

set.remove(8)
print(set)

set.clear()
print(set)


thisdict = {"name": "pigeon","type": "bird",
           "skin cover": "feathers"}

print(thisdict)

x = thisdict.get("type")
print(x)


thisdict["skin cover"] = "skin color"
print(thisdict)