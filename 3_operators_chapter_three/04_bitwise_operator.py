# bitwise operator in python is used to perform operations on individula bits of binary number.
# and bitwise operator only works on integer, which means integers are first converted into binary and then operations are performed on each bit.

# rule of bitwise operator
"""
1. align number from right side
2. add leading zeros if needed
3. and bitwise operator returns the result in decimal by default
"""

# list of bitwise operator
"""
Operator                      Name
   &                       Bitwise AND
   |                       Bitwise OR
   ^                       Bitwise XOR
   ~                       Bitwise NOT
   >>                      Bitwise right shift
   <<                      Bitwise left shift
"""
# now we will see each operator in detail

#------------------------------------------------------------------------------------

# Bitwise AND (&)
# the bitwise AND compares two integers bit by bit, and if both corresponding bits are 1 the it will return 1 otherwise it will return 0 
x_and = 23  #   10111   binary of 23
y_and = 93  # 1011101   binary of 93
            #   10101   binary of 21
print(x_and & y_and)
print("\n")

#------------------------------------------------------------------------------------

# Bitwise OR (|)
# the bitwise OR compares two integers bit by bit, and if any one of the bit is 1 then it will return 1, and if both the bits are 0 then it will return 0
x_or = 83 # 1010011   binary of 83
y_or = 52 #  110100   binary of 52
          # 1110111   binary of 119
print(x_or | y_or)
print("\n")

#------------------------------------------------------------------------------------

# Bitwise XOR (^)
# the bitwise XOR compares two integers bit by bit , if both the bits are different then it will return 1 , and if both the bits are different then it will return 0 
x_xor = 73 # 1001001   binary of 73
y_xor = 62 #  111110   binary of 62
           # 1110111   binary of 119
print(x_xor ^ y_xor)
print("\n")

#------------------------------------------------------------------------------------

# Bitwise NOT (~)
# bitwise NOT flips bits which means if the bit is 1 then it will convert it to 0 and vice-versa, and bitwise NOT operator only accepts one operand
x_not = 23 # 10111   binary of 23
print(~ x_not)
"""
now you can think why we get -24 and it's binary value will be 11101000, but we should get 8 and its binary value is 01000

+ first understand why we are getting value's in negative?
- Python represents negative integers internally using two's complement, because computer cannot store negative sign in binary
  Two's complement is a method computers use to represent negative numbers in binary.
  Computers only understand 0 and 1.
  To represent negative numbers using only 0 and 1, two's complement is used.
 

+ now we will understand why we got -24
- computer doesn't store numbers using only the minimum bits needed
  so they store numbers using a fixed number of bits(8-bit, 16-bit, 32-bit, 64-bit, etc.)
  python behaves like it has infinite bits.


+ now we will see how python calculate's it internally, in 8-bit format
- step 1:
    23 in 8-bit binary: 00010111

    Apply bitwise NOT (flip all bits):
    11101000   ← This is the result after flipping bits

    Since the leftmost bit is 1, this represents a negative number
    (in signed two's complement representation).
 
  step 2:
    To find its decimal value, take two's complement again:
    11101000
    flip this bit then add 1 to it 
    00010111
    +      1  # here you want to do binary addition
    --------
    00011000  = 24  

    so the value is -24
"""
# so I hope after this you can understand why we got -24
print("\n")

#------------------------------------------------------------------------------------

# Bitwise right shift (>>)
# it shift bits to right
x_right = 12  # 1100   binary of 12
print(x_right >> 2) 

"""
It shifts all bits to the right by 2 positions, and the bits shifted out from the right are discarded
here is the representation

00001100  (binary of 12)
>> 2
----------------
00000011  (binary of 3)
"""
print("\n")

#------------------------------------------------------------------------------------

# Bitwise left shift (<<)
# it shift bits to left
x_left = 41 # 101001   binary of 41
print(x_left  << 1)

"""
It shifts all bits to the left by 1 positions, and the bits shifted out from the left are discarded
here is the representation

00101001   (binary of 41)
<< 1
----------------
01010010   (binary of 82)
"""
  
#------------------------------------------------------------------------------------

"""

operator precedence in bitwise operator 
~
<< >>
&
^
|

"""