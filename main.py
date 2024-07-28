txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Ahmed", "Ali", "Saeed")

def my_functions(**kid):
  print("His last name is " + kid["lname"])

x = lambda a : a

import time

print(dir(time))

x = 1
for i in range(5):
  print("*" * x)
  x += 1
for i in range(x):
  print("*" * x)
  x -= 1


txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)



# Method	              Description
#capitalize()	    Converts the first character to upper case
#casefold()	      Converts string into lower case
#center()	        Returns a centered string
#count()	        Returns the number of times a specified value occurs in a string
#encode()   	    Returns an encoded version of the string
#endswith()	      Returns true if the string ends with the specified value
#expandtabs()	    Sets the tab size of the string
#find()	          Searches the string for a specified value and returns the position of where it was found
#format()	        Formats specified values in a string
#format_map()	    Formats specified values in a string
#index()	        Searches the string for a specified value and returns the position of where it was found
#isalnum()	      Returns True if all characters in the string are alphanumeric
#isalpha()	      Returns True if all characters in the string are in the alphabet
#isascii()	      Returns True if all characters in the string are ascii characters
#isdecimal()	    Returns True if all characters in the string are decimals
#isdigit()	      Returns True if all characters in the string are digits
#isidentifier()	  Returns True if the string is an identifier
#islower()	      Returns True if all characters in the string are lower case
#isnumeric()	    Returns True if all characters in the string are numeric
#isprintable()	  Returns True if all characters in the string are printable
#isspace()	      Returns True if all characters in the string are whitespaces
#istitle()	      Returns True if the string follows the rules of a title
#isupper()	      Returns True if all characters in the string are upper case
#join()	          Joins the elements of an iterable to the end of the string
#ljust()	        Returns a left justified version of the string
#lower()	        Converts a string into lower case
#lstrip()	        Returns a left trim version of the string
#maketrans()	    Returns a translation table to be used in translations
#partition()	    Returns a tuple where the string is parted into three parts
#replace()	      Returns a string where a specified value is replaced with a specified value
#rfind()	        Searches the string for a specified value and returns the last position of where it was found
#rindex()	        Searches the string for a specified value and returns the last position of where it was found
#rjust()	        Returns a right justified version of the string
#rpartition()	    Returns a tuple where the string is parted into three parts
#rsplit()	        Splits the string at the specified separator, and returns a list
#rstrip()	        Returns a right trim version of the string
#split()	        Splits the string at the specified separator, and returns a list
#splitlines()	    Splits the string at line breaks and returns a list
#startswith()	    Returns true if the string starts with the specified value
#strip()	        Returns a trimmed version of the string
#swapcase()	      Swaps cases, lower case becomes upper case and vice versa
#title()	        Converts the first character of each word to upper case
#translate()	    Returns a translated string
#upper()	        Converts a string into upper case
#zfill()	        Fills the string with a specified number of 0 values at the beginning

hell = "Hello, World!"

print(hell.endswith("d!"))

print(hell.find("o"))
print(hell.rfind("o"))

#There are four collection data types in the Python programming language:

#  List - is a collection which is ordered and changeable. Allows duplicate members.
#  Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
#  Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#  Dictionary - is a collection which is ordered** and changeable. No duplicate members.

mylist = ["apple", "banana", "cherry"]
mytuple = ("apple", "banana", "cherry")
myset = {"apple", "banana", "cherry"}
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
del thislist

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in range(51) if (x%2) == 0]
print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict["year"] = 2018
thisdict.update({"year": 2020})
thisdict["color"] = "red"
thisdict.update({"color": "Black"})
print(thisdict)

thisdict.pop("model")
thisdict.popitem()
del thisdict["brand"]
print(thisdict)
thisdict.clear()
del thisdict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Mohammed",
    "year" : 2004
  },
  "child2" : {
    "name" : "Ahmed",
    "year" : 2007
  },
  "child3" : {
    "name" : "John",
    "year" : 2011
  }
}

child1 = {
  "name" : "Mohammed",
  "year" : 2004
}
child2 = {
  "name" : "Ahmed",
  "year" : 2007
}
child3 = {
  "name" : "John",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])




a = 200
b = 33

if a > b: print("a is greater than b")

print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

if b > a:
  pass

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(2, 20, 3):
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


for x in [0, 1, 2]:
  pass

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def myfunction():
  pass # avoid getting an error

# To specify that a function can have only positional arguments, add , / after the arguments
def my_function(x, /):
  print(x)
my_function(3)

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

def myconverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

#Formatting Types
# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding Unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 17
name = "Ahmed"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

for i in range(1, 100):
  print(i)


for x, i in enumerate([3, 4, 5, 6]):
  print(x ,i)

