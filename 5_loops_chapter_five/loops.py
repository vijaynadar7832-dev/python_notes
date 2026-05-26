# Loops in python are used to exectute a block of code repeatedly until a condition is met or all items in the sequence are processed
# Loops are used in tasks like processing data, automating repetatice tasks, and iterating through collections like (strings, lists, etc)

#--------------------------------------------------------------------------------------------------------------------------

# For loop 
# for loop is used when you know how many times you want to repeat something or when you want to iterate over a sequence.

# for loop syntax
"""
for variable in sequence:
    # code block
"""

# for loop example 1 
print("loop through list")
fruits = ["Apple" , "Banana" , "Pineapple" , "Watermelon" , "Kiwi" , "Orange" , "Muskmelon" , "Grapes" , "Mango"]
for i in fruits:
    print(i)
print("\n")

# for loop example 2
print("using range()")
for i in range(0 , 20 , 2):
    print(i)

#--------------------------------------------------------------------------------------------------------------------------

# While Loop
# the while loop runs as long as the given condition remains True. When the conditon becomes False , the line immediately after the loop in the program is executed
# Be careful: if the condition never becomes false in while loop, it creates an infinite loop. 

# While loop syntax
"""
while condition:
    # code block
"""

# While loop example

# while loop example 1
i = 1
while i <= 5:
    print(i)
    i += 1

# while loop example 2
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access Granted")

#--------------------------------------------------------------------------------------------------------------------------

# Nested loop 
# a loop inside another loop 

# example
for i in range(3):
    for j in range(3):
        print(i,j)

#--------------------------------------------------------------------------------------------------------------------------

# loop with else

# example
numbers = [1 , 2 , 3 , 4 , 5]
usr_input = int(input("enter a number: "))
for i in numbers:
    if i == usr_input:
        print("found")
        break
else:
    print("not found")


#--------------------------------------------------------------------------------------------------------------------------

# Loop control statements

# break : stops the loop immediately.
for i in range(5):
    if i == 3:
        break
    print(i)

# continue : skips the current iterationa and moves to the next.
for i in range(8):
    if i == 5:
        continue
    print(i)

# pass : it is used as a temporary placeholder but it does nothing, Sometimes Python requires a block of code, but you have not written it yet.Without pass, Python gives error because an empty block is not allowed. 