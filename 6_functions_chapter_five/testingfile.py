# question 1

def addition(a,b):
    return a+b

result = addition(20 , 84)
print(result)

print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 2

def substract(a,b):
    return a-b

print(substract(50 , 20))

print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 3

def is_even(number):
    if number % 2 == 0:
        return "True"
    else:
        return "False"

print(is_even(3))
print(is_even(22))

print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 4

def area_of_rectangle(length , width):
    area = length * width
    return area

area_of_rect = area_of_rectangle(10 , 5)

print(area_of_rect)

print("\n")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 5

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

print(maximum(35 , 93))
print(maximum(62 , 61))

print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 6

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

print(square(cube(2)))

print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 7

def add(a,b):
    return a+b

def double(number):
    return number * 2

answer = double(add(10, 15))
print(answer)
print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 8

def student_result(marks):
    if marks < 0 or marks > 100:
        return "enter a valid marks"
    elif marks >= 40:
        return "pass"
    else:
        return "Fail"

print(student_result(75))
print(student_result(20))

print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 9

def calculator(a , b , operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    else:
        return a/b
print(calculator(3 , 4 , "+"))
print(calculator(3 , 4 , "-"))
print(calculator(3 , 4 , "*"))
print(calculator(3 , 4 , "/"))

print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# question 10

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def square(number):
    return number ** 2

print(square(multiply(add(2,3),4)))






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# first_name = input("enter your first name:")
# second_name = input("enter you second name:")
# live_place = input("enter the place where you live:")
# status = input("are you employed or unemployed:") 

# def personal_info(first_name , second_name , live_place , status):
#     print("Hi")
#     print(f"My name is {first_name} {second_name}")
#     print(f"I live in {live_place}")
#     print(f"I am {status}")

# personal_info(first_name , second_name , live_place , status)



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++



# def personal(first_name , last_name , place):
#     print(f"my name is {first_name} {last_name}")
#     print(f"I live in {place}")

# personal("vijay","nadar","Thane")



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

# One function calling another function

# def greeting():
#     print("hi")
#     print("welcome")

# def personal_info(first_name , last_name, place):
#     greeting()
#     print(f"my name is {first_name} {last_name}")
#     print(f"I live in {place}")

# personal_info("naruto" , "kumar" , "bihar")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def calculator(a , b , operator):
    if operator == "+":
        return a+b 
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a*b
    else:
        return a/b
print(calculator(3 , 4 , "/"))

print("\n")