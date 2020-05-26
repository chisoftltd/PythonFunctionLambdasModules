# PythonFunctionLambdasModules by ChisoftMedia

# Calling a Function
import os
import platform
import time
import mymodule as mx
import mymodule
from mymodule import person1
from time import sleep



def my_function():
    print("Hello from my function!")

my_function()

# Arguments
def my_function(firstName):
    print(firstName + " is your FirstName")

my_function("Joy")
my_function("Benjamin")
my_function("Shepherd")
my_function("Mikael")

def my_function(firstName, lastName):
    print(firstName + "  " + lastName + " is your Name")

my_function("Joy", "Chinwe")
my_function("Benjamin", "Chinwe")
my_function("Shepherd", "Chinwe")
my_function("Mikael", "Chinwe")

# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[1])

my_function("Emmanuel", "Mikael", "Shepherd")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emma", child2 = "Shae", child3 = "Miknwa")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"] + " " + " and The first name is " + kid["fname"])

my_function(fname = "Emma", lname = "Chinwe")

# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
def myfunction():
  pass

# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print(tri_recursion(60))

################
# Python Lambda
################

a = lambda x : x + 10
print(a(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b : a + b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(10, 11, 13))

# Why Use Lambda Functions?
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(6)
print(mydoubler(11))

print()
print()

mytripler = myfunc(3)
print(mytripler(11))



# Use a Module
mymodule.greeting("Benjamin")

# Variables in Module
a = mymodule.person1["age"]
print(a)

# Re-naming a Module
a = mx.person1["Country"]
print(a)

# Built-in Modules
x = platform.machine() # .system()
print(x)

k = platform.system()
print(k)

# Using the dir() Function
x = dir((platform))
print(x)

# Import From Module
a = person1["name"]
print(a)