# In this section we will see about functions
# A function is a reusable block of code that performs a specific task. It allows us to write code once and use it many times.

#-----------------------------------------------------------------------------------------------------------------------------

"""
# Why do we use functions?
- suppose you don't use function's

""
print("Hello Vijay")
print("Welcome")
print("Have a nice day")

print("Hello Vijay")
print("Welcome")
print("Have a nice day")

print("Hello Vijay")
print("Welcome")
print("Have a nice day")
""

- here you can see that the same code is repeated, this is called duplicate code.
- so instead of writting the same thing mulitple time we can use a funtions like the given below example:

""
def greeting():
    print("Hello Vijay")
    print("Welcome")
    print("Have a nice day")
greeting()
greeting()
greeting()
""
- now we can see that this code is shorter, cleaner, and much easier.

"""

#-----------------------------------------------------------------------------------------------------------------------------

"""
# Why functions are important?
- Functions helps us 
  > Reuse code
  > Reduce duplicate code
  > Make programs shorter
  > Make code easier to understand
  > Make debugging easier
  > Divide large programs into small pieces
"""

#-----------------------------------------------------------------------------------------------------------------------------

# Types of functions
# There are majorly two types of functions 

# 1. Built-In Functions
# Python built-in function are predefined functions that are globally available in the Python interpreter without requiring any import statement.
# Python built-in functions are written directly into the core language to perform everyday tasks efficiently, optimize code execution, speed, and keep the source code hightly readable.
# Python includes over 70 built-in functions. These are the most common ones divided by their utility, below is the given official documentation link where you can find all built-in functions 
"""https://docs.python.org/3/library/functions.html"""
# example of some built-in functions: "print()" , "len()" , "abs()", etc. Check out the above given link to find all the python built-in functions


# 2. User-Defined Function
# A User-Defined Function in python is a custom, reusable block of code created by a programmer to perform a specific task. Unlike built-in functions like print() or len(), which are automatically available in python, a user-defined function is written manually to handle unique logic.

# Example of user-defined functions:
def sample(a,b):
    print(a+b)

sample(3 , 2)

print("\n")

#-----------------------------------------------------------------------------------------------------------------------------

# Now we will see the structure of a function

