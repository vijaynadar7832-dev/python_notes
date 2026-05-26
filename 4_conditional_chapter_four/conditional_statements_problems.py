"""
Q: Even or Odd 
   write a program that takes a number from the user and checks wether the number is: Even OR Odd
"""
# first method
num_1 =  int(input("enter a number: "))

if num_1 % 2 == 0:
    print("number is even")

else:
    print("number is odd")



# second method
num_2 = int(input("enter a number: "))

if num_2 % 2 != 0:
    print("number is odd")

else:
    print("number is even")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Largest of Three Number
   write a program that takes three numbers form the users and prints the largest number among then
"""

num_3 = int(input("enter First number: "))
num_4 = int(input("enter Second number: "))
num_5 = int(input("enter Third number: "))

if num_3 == num_4 == num_5:
    print("all the numbers are equal")

elif num_3 > num_4 and num_3 > num_5:
    print(num_3)

elif num_4 > num_3 and num_4 > num_5:
    print(num_4)

elif num_5 > num_4 and num_5 > num_3:
    print(num_5)

elif num_3 < num_4 and num_4 == num_5:
    print(num_4)

elif num_4 < num_3 and num_3 == num_5:
    print(num_3)

elif num_5 < num_3 and num_3 == num_4:
    print(num_3)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Student Grade System
   write a program that takes marks from the user prints the grade according to the following codintions:
        Marks                                     Grade
        90-100                                      A
        75-89                                       B
        50-74                                       C
        35-49                                       D
        Below 35                                   Fail
    Also handle marks less than 0 and greater than 100
"""

marks = int(input("Enter your marks: "))

if marks < 0:
    print("Enter a valid Marks")

elif marks > 100:
    print("Enter a valid Marks")

elif marks >= 90 and marks <= 100:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

elif marks >= 35:
    print("Grade D")

elif marks < 35 and marks >= 0:
    print("Fail")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: ATM Withdrawal System
   Write a program for an ATM machine
   The program should:
   1. Ask the user for account balance
   2. Ask for withdrawal amount
   3. Apply the following conditions:
      - If the withdrawal amount is less than or equal to balance:
         - Withdrawal success
         - Deduct balance
      - If the withdrawal amount is greater than balance:
         - Print "Insufficient balance"
      - If withdrawal amount is less than or equal to 0:
         - Print "Invalid withdrawal amount"
   Finally Print the remaining balance if transaction is successful.
"""

balance = int(input("Enter your Balance amount in your account: "))
withdraw = int(input("Enter your Withdrawal amount form your account: "))

if balance < 0:
    print("Enter valid Balance amount")

elif withdraw <= 0:
    print("Enter valid Withdrawal amount")

elif withdraw <= balance:
    print("Withdrawal Successful")
    print(f"Your remaining Account Balance is: {balance - withdraw}")

elif withdraw > balance:
    print("Insufficient Fund")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Login Systems with Multiple Conditions
   Create a simple login system.
   -Conditions:
      -correct username: "admin"
      -correct password: "python123"
   -Program Behavior:
      1. Ask user for name.
      2. Ask user for password.
   -Cases:
      -If both are correct:
         -print "Login Successful"
      -If username is wrong:
         -Print "Invalid Username"
      -If username is correct but password is wrong:
         -Print "Incorrect Password"
"""

username = input("Enter your Username: ")
password = input("Enter your Password: ")

if username == "admin" and password == "python123":
    print("Login Successful")

elif username != "admin":
    print("Invalid Username")

elif password != "python123":
    print("Incorrect Password")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

