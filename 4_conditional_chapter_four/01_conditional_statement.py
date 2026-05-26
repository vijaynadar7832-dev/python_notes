# conditional statements is used to make decisions in a program
# they allow python to execute different blocks of code depending on whether a condition is True or False


# 1. if statement
""" if statement is the simplest from of conditional statement
    The if statement checks a condition. if the condition is True then the code inside the if block will execute, and it the input is not matched to the condition then it will not print anything in the output """

age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible to vote")

#--------------------------------------------------------------------------------------

# 2. if-else statement
""" sometimes we need two actions first one is if the condition is true and another one is if the condition is false
    In this case the if-else statement is used """

"""
age_2 = int(input("enter your age: "))
if age_2 <= 5 and age_2 > 0:
    print("ticket is free")
else:
    print("you need to pay for the ticket")
"""

# In the above example we see that if we entered the negative value of the 0(zero) value then it goes under the else condition
# So to prevent this we cannot directly give coditions to else statement so we will use the nested if and else statement

age_3 = int(input("enter your age: "))
if age_3 <= 5 and age_3 > 0:
    print("you are eligible for free ticket")
else:
    if age_3 <= 0:
        print("enter a valid age")
    else:
        print("you need to pay for the ticket")

# so by using nested list we can prevent the negative integer and 0 value by accepting in the input 

#--------------------------------------------------------------------------------------

# 3 elif statement
""" elif statemnt in python stands for " else-if " statement. It allows us to check multiple conditions, and we use elif when there are multiple conditons."""

marks = int(input("enter your marks to check your grade: "))
if marks > 100:
    print("Enter marks between 0 to 100")
elif marks < 0:
    print("Enter a valid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 55:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
elif marks >= 20:
    print("Grade F")
else:
    print("Grade G: YOU HAVE NO RIGHTS TO GET THE EDUCATION")

#--------------------------------------------------------------------------------------

# Ternary operator in conditional statement

# Ternary operator in python most accuratly called as conditional expression let you write a simple if-else statment in one line 

x = int(input("Enter your age: "))
status = "adult" if x >= 18 else "minor"
print(status)