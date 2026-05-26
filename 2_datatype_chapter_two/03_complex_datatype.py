# Here we will learn about complex datatype in detail
 
# in complex numbers there are two parts which is 
  # complex numbers = real part + imaginary part

# in mathematics complex number is written as 3 + 4i
# but in python i is written as j for example z = 3 + 4j


# now we will see how to write complex numbers, complex numbers can be written in two forms which are by using direct assignment and also using complex() funcitons 

# first type / using direct assignment
z1 = 2 + 3j
z2 = -2 + 3j
z3 = 3j  # here real part is zero
print(z1)
print(z2)
print(z3)
# not If we write like z = 3 then it will be integer not the  

# second type / using complex() function 
z = complex(2 , 4)
print(z) # here output will be 2+4j
# here one thing to note that If we write like z = complex(2) the here it will be 2+0j , which means whatever we are writing inside the bracket will be real part not an imaginary part

# lets do type checking 
print(type(z))

# now we will see how to access the real and the imaginary part, the python provides the built-in attributes 
t = complex(3 , 7)
print(t.real) # It prints the real part 
print(t.imag) # It prints the imaginary part 
# here note that values are returned as float


# Arithmetic operations on complex Numbers

add_a = 3 + 3j
add_b = 3 + 3j
print(f"addition of two complex number : {add_a + add_b}")

sub_a = 3 + 5j
sub_b = 3 + 4j
print(f"substraction of two complex number : {sub_a - sub_b}")

mul_a = 3 + 8j
mul_b = 8 + 3j
print(f"multiplication of two complex number : {mul_a * mul_b}")

div_a = 3 + 2j
div_b = 3 + 6j
print(f"division of two complex number : {div_a / div_a}")


# comparison with complex number
comp_a = 3 + 3j
comp_b = 2 + 8j
print(comp_a == comp_b) # here we are comparing if both are equal it will return true otherwise it will return false
print(comp_a != comp_b) # here we are comparing if both are equal it will return false otherwise it will return true 
# python cannot compare complex number directly using < or > , if we try to do it will return error


# Now we will see how to get the magnitude of the complex number , which in python we called as absolute value
# basically in mathematics the formula for the magnitude is ∣a+bi∣ = √(a^{2}+b^{2}) , if this is not clear just go to google and search magnitude of complex number
magnitude_a = 3 + 2j 
print(f"magnitude of 3 + 2j is : {abs(magnitude_a)}")


# Now we will see the conjugate of complex number
# conjugate changes the sign of the imaginary part, we will see below
conjugate_a = 9 + 7j
print(f"conjugate of 9 + 7j is : {conjugate_a.conjugate()}")
