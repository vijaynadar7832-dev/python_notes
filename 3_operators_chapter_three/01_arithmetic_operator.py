# arithmetic operations in python is used to perform mathematical calculations on number such as integers and floating point numbers
# arithmetic operators are special symbols that tells python to perform mathematical operations like addition , substraction , multiplication , etc.

# there are 7 types of arithmetic operators
"""
Operators                   Name
    +                       Addition
    -                       Subtraction
    *                       Multiplication
    /                       Division
    //                      Floor Division
    %                       Modulus(remainder)
    **                      Exponent(power)
"""

# Now we will see each operators in detail

#------------------------------------------------------------------------------------

# Addition (+)
add_a = 23 
add_b = 64
add_c = 83.2

print(add_a + add_b)
print(add_b + add_c , type(add_b + add_c)) # when we add int and float , then python automatically converts int to float
# python allows addition between two numeric types
print("\n")

#------------------------------------------------------------------------------------

# Sustraction (-)
sub_a = 52
sub_b = 42
sub_c = 21.53

print(sub_b - sub_a)
print(sub_a - sub_c , type(sub_a - sub_c)) # when we subtract int and float , then python automatically converts int to float
# python allows you to subtract between different numeric type
print("\n")

#------------------------------------------------------------------------------------

# Multiplication (*)
multi_a = 32
multi_b = -12
multi_c = 23.53

print(multi_a * multi_b)
print(multi_a * multi_c , type(multi_a * multi_c)) # when we multiply int and float , then python automatically converts int to float
# python allows you to multiply between different mumeric type

#------------------------------------------------------------------------------------

# Division (/)
div_a = 10
div_b = 2
div_c = 6.4

print(div_a / div_b , type(div_a / div_b)) # division always returns value in float even through the value is integer
print(div_a / div_c , type(div_a / div_b))
# python allows you to divide between different number datatype

#------------------------------------------------------------------------------------

# Floor Division (//)
# floor division returns the largest integer less than or equal to the result
floor_a = 10 
floor_b = 3
floor_c = -5

print(floor_a // floor_b , type(floor_a // floor_b)) # here  if we do division we will get answer as 3.333335 but if we use the floor division you will get 3
print(floor_c // floor_b , type(floor_c // floor_b)) # floor division with negative value, here you can get confused why? -2 if we divide we will get -1.66667 , Because Python goes to the lower integer, not toward zero. if we see in number line -2 is lowest number than -1.6

#------------------------------------------------------------------------------------

# Modulus (%) (remainder)
mod_a = 41
mod_b = 3 
mod_c = -32
mod_d = -5

print(mod_a % mod_b)
print(mod_c % mod_b) # answer will be in positive 
print(mod_a % mod_d) # answer will be in negative 
# NOTE = always remember modulus result always has the same sign as the divisor , not the dividend

#------------------------------------------------------------------------------------

# Exponent (**) (power operator)
exp_a = 4
exp_b = -2

# square root
print(exp_a ** 5) # 4*4*4*4*4 = 1024
print(exp_b ** 3) # -2*-2*-2 = -8

# cube root
print(41 ** (1/3)) # so to get cube root use this (value ** (1/3))