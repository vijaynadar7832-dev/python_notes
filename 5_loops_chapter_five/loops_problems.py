"""
Q: Multiplication Table
   Take a number from the user and print it's multiplication table from 1 to 10 using a loop
"""

number = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

user_input = int(input("enter a number to get the multiplaction table: "))

for i in number:
    print(f"{user_input} X {i} = {user_input * i}")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Count Digits
   Take a integer input and count how many digits are present in the number.
"""

user_input2 = input("Enter a number to count it's lenght: ")
count = 0 

for i in user_input2:
   count += 1
print(count)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Sum of Digits
   Take a number from the user and calculate the sum of it's digits using a while loop
"""

# using for loop

user_input3 = input("enter more than one digit number to find it's sum: ")

count_2 = 0

for i in user_input3:
   count_2 += int(i)

print(count_2)


# using while loop

user_input4 = int(input("enter a multi digit number: "))

count_3 = 0

while user_input4 > 0:
   extract_last_number = user_input4 % 10
   count_3 += extract_last_number
   user_input4 //= 10

print(count_3)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Factorial of a Number
   find the factorial of a number using a loop
"""

user_input5 = int(input("enter a number to find it's factorial: "))
dub = user_input5

count_4 = 1

while user_input5 > 0:
   count_4 *= user_input5
   user_input5 -= 1
print(f"the factorial for {dub} is: {count_4}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Number Guessing Program
   Create a guessing game where:
    - A secret number is already stored.
    - User keeps entering number.
    - Loop continues until correct guess.
"""

number_2 = int(input("Enter any four digit number: "))

while number_2 != 1111:
   number_2 = int(input("Retry and guess the correct number: "))
print("U got the correct number")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Fibonacci Series
   Print first n fibonacci number using loop
"""

usr_input = int(input("enter a number to find it's factorial: "))

a = 0
b = 1

for i in range(usr_input):
   if a > usr_input:
      break

   print(a)

   c = a + b 
   a = b
   b = c

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Q: Prime Number Check
   take a number from the user and check whether it is prime or not, using loop
"""

