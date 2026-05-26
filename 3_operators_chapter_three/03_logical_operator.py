# Logical operator in python is used to combine or modify conditions and it returns result in boolean either True or False, They are commonly used in conditional statements to control the flow of the program based on multiple logical conditions

"""
there are 3 logical operators in python which are:

and 
or 
not 
"""
# Now we will see each operators in detail

#------------------------------------------------------------------------------------

# and operator
# and returns True only if both the conditions are True
"""
let's see the truth table for AND operator
 A              B                A and B
True           True                True
True           False               False
False          True                False
False          False               False
"""
# let's see some example
y = 32
print(y < 62 and y > 21)
print(y > 51 and y < 61)
# you can see above that if any one of the condition is False then it will return as False
print("\n")

#------------------------------------------------------------------------------------

# or operator
# or returns True if atleast one condition is True
"""
let's see the truth table for or operator
 A              B                 A or B
True           True                True
True           False               True
False          True                True
False          False               False
"""
# let's see some example
x = 92
print(x < 121 or x < 42 or x > 312)
print(x > 144 or x < 21)
# you can see above if any one of the condition is True then it will return True
print("\n")

#------------------------------------------------------------------------------------

# not operator
# not operator is used to reverse the result
"""
 A                notA
True              False  
False             True
"""
# let's see some example
not_a = 23 < 42 or 32 > 81
print(not_a)
print(not not_a)
print(not 23 > 41)
# here you can see the inverse of the result

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# important concept: Short-Circuiting
# python stops checking once it know the result, let's see example

# and Short-Circuit
# if first condition is False, python will not check the next condition operator in and operator
print(False and print("hello")) # here you can see hello is not printed, because first condition is False so python doesn't check next condition 

# or Short-Circuit
# if first condition is True, python will not check the next condition in or operator
print(True or print("hello")) # here you can see hello is not printed, because first condition is True so python doesn't check next condition 
print("\n")

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# Logical operator precedence
"""
not 
and 
or
"""
# let's see one example

print(True or False and False)
# step 1: False and False -> False
# step 2: True or False -> True

# NOTE :- Parentheses () can always be used to override the default operator precedence
# Example
print((True or False) and False) # here you can see even through and comes first in operator precedence then or, but due to the use of parentheses (), so first the condition inside the parentheses is given the priority 