# comparison operator in python are used to compare two values an always the result value will be in boolean either true or false

# list of comparison operators
"""
Operator                          Names
   ==                             Equal to 
   !=                             Not Equal to 
   >                              Greater than
   <                              Less than
   >=                             Greater than or Equal
   <=                             Less than or Equal 
"""
# Now we will see each operator in detail

#------------------------------------------------------------------------------------

# Equal to (==)
print("Equal to")
print(2 == 3)
print(32 == 32)
print("apple" == "Apple") # while string python calculate on the basis of ascii / unicode
print(True == 1) # internally True = 1 
print(False == 0) # internally False = 0
print("\n")

#------------------------------------------------------------------------------------

# Not Equal to (!=)
print("Not Equal to ")
print(23 != 23)
print(53!= 42)
print("orange" != "Orange")
print([1 , 2 , 3] != [2 , 2 , 3]) # comparision between list
print("\n")

#------------------------------------------------------------------------------------

# Greater than
print("Greater than")
print(523 > 234)
print((2 , 3 , 4) > (3 , 3)) # comparision between tuple
print("Bat" > "Batman")
print("\n")

#------------------------------------------------------------------------------------

# Less than 
print("Less than")
print(23 < 53)
print("Site" < "Zebra")
print("\n")

#------------------------------------------------------------------------------------

# Greater than or Equal
print("Greater than or Equal")
print(45 >= 42)
print(32 >= 31)
print("Night" >= "Fall")
print("\n")

#------------------------------------------------------------------------------------

# Less than or Equal 
print("Less than or Equal")
print(23 <= 23)
print(53 <= 62)
print("\n")

#------------------------------------------------------------------------------------


# print("32" == 32)  ❌ it will give you error 

# you can use comparison operator with all datatype but COMPLEX datatype only supports EQUALITY checking

