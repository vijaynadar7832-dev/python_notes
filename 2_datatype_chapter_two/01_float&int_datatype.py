# the float datatype in python is used to represent real numbers with fractional component(decimal point)

a = 34.3
b = -7.3
c = 3.0
# all of the above are float datatype

print(type(a) , type(b) , type(c))






#____________________________________________________________________________________________________________________________________________________________________________________________________________






# Here we will see int datatype in python 

a_int = 54
b_int = -32
c_int = 0
d_int = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

print(a_int ,b_int , c_int , d_int , sep="\n") # inside the print function we used a sep= '"\n"', and \n is escape sequence which is used to print output in next line in next line
print("") # here this is used to give a 1 line space 
# in above program we have seen in which type we can give the literal to store inside the variable 
# we can store only integers values, which can be positive, negative, zero(0), or infinite number
# and in python we can store infinite numbers and it will never throw any error, it can store value till memory is full



x = 75
y = 33
z = x + y
print(x , type(x), id(x), sep="\n")
print("")
print(y , type(y), id(y), sep="\n")
print("")
print(z , type(z), id(z), sep="\n")
# here we will learn some built-in functions which can be helpful
# type() function is used to print the literal datatype
# id() function is used to check the memory location of literal/object and it is Useful to check whether two variables reference the same object or different objects.
# print() even i ask to coma patient that what is the use of print() funtion he will explain you, so let's move further
print("")



print("now we will see how python supports different number system")
int_Decimal = 1999 
int_Octal = 0o65743  # octal number system which is 10 base to 8 where number starts from "0, 1, 2, 3, 4, 5, 6, 7" in octal first we want to write "0o" then we can add the mentioned numbers only
int_HexaDecimal = 0x4f43 # hexa-decimal number system which is 10 base to 16 where number starts from "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f" in hexa-decimal first we want to write "0x" then we can add the mentioned numbers and letters only
int_Binary = 0b1001010 # binary number system which ony consist 2 numbers which is "0, 1"in binary first we want to write "0b" then we can use the number 0 and 1 to write a number in binary
print(int_Decimal , int_Octal , int_HexaDecimal , int_Binary , sep="\n")
print("")




print("now we will see how to convert one number system to another") 
to_Octal = oct(int_Decimal) # here we converted decimal to octal number system
to_HexaDecimal = hex(int_Decimal) # here we converted decimal to hexa-decimal number system
to_Binary = bin(int_Decimal) # here we converted decimal to binary number system
print(to_Octal , to_HexaDecimal , to_Binary , sep="\n")
# some guys can raise doubt that how to convert other number system to decimal, motherfucker we always get output in 10 base to 10 number system which we use everywhere 
print("")



# now we will learn type conversion in int datatype
print(int(3.9)) # (fraction part is truncated, not rounded) here we are doing truncating which means it will point to the origin(0,0) 
print(int("23")) # it will convert string to integer
print(int(True)) # True means '1'
print(int(False)) # False means '0'
# print(int("hello"))  # this will throw an invalid conversion error because we can only convert numbers in int type conversion 
print("")
print("")



# now we will see operations in integer
# frist we will see about Arithmetic operators
# 1.Arithmetic Operator
a = 27
b = 9
# to print here we used formated string literal
print(f"addition: {a + b}")  # here we are performing addition of two numbers 
print(f"substraction: {a - b}") # here we are performing substraction of two numbers
print(f"multiplication: {a * b}") # here we are performing multiplication of two numbers
print(f"division: {a / b}") # here we are performing division of two numbers
print(f"modulo: {a % b}") # here we are performing modulo of two numbers
print(f"exonent: {a ** b}") # here we are calculating power of value a
print(f"negation: {a} = {-a}") # negation is used to convert positive digit to negative and vice-versa
print(f"integer division: {a // b}") # this is called as floor division which is used to remove the value after decimal
