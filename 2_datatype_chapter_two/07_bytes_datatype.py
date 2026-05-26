# bytes are a built-in immutable datatype in python used to store and represent raw binary data as a sequence of integers ranging from 0 to 255
# why bytes datatype exists ?
# because many real world things are not texts, they can be image, audio, video, network packets, encrypted data, file on disk; all this are stored as bytes not as a string 
"""first we will understand why bytes only allows value from 0 to 255
   1. A bit is a smallest unit of data so it can only be 0 or 1 nothing else
   2. what is byte?
      1 byte = 8 bits
      example = 01010111 # this is one byte
   3. So how many values can 8 bit store?
      each bit has 2 possibilties: 0 or 1
      So:
      2*2*2*2*2*2*2*2
      = 2^8
      = 256 values
   4. Computer starts counting from 0, not from 1
      so the value becomes 0 to 255
      total value = 256
   5. visualization (for understanding)
         binary                          decimal
        00000000                            0
        00000001                            1
        00000010                            2
        ......                             ....
        11111111                           255
      after this there is no space left inside 8 bits, to store 256 you would need 100000000 (9 bits) , which is not a byte anymore
"""

# now we will see immutability in bytes datatype
"""
immutable = bytes(52)
immutable[0] = 76
print(immutable)
""" # If we run this code it will give type error :bytes object does not support item assignment





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# Now we will see the syntax of bytes datatype



# SYNTAX 1 b" " (bytes literal)
syntax_1 = b"hello"
print(syntax_1 , type(syntax_1), sep="\n")
print("\n")
# here you can get doubt that earlier you told that bytes datatype can only store from number 0 to 255, then how we stored the string value: python internally converts each character into ASCII numeric value
# so actually it becomes something like this h = 104 , e = 101 , l = 108 ... and so on , but when it displays output it shows in readable form
# But b" " only store ASCII character from 0 to 127 other than that we can't store any emoji or other character which is outside the ASCII character; we will see one example below
"""
emoji = b"🖕🏼"
print(emoji , type(emoji))
""" # once you comment out this and run the code you will get syntax error mentioned bytes can only contain ASCII literal characters, and other than ascii values it takes multiple bytes , so we get error

# But there is a way to print and store the emoji in bytes, we will see below 
# we will use the .encode() and .decode() method to print the non ascii values
emoji_encode = "🖕🏼".encode()
print(emoji_encode , type(emoji_encode))
emoji_decode = emoji_encode.decode()
print(emoji_decode , type(emoji_decode))
print("\n")



# SYNTAX 2 bytes() "bytes constructor" using list
# in this syntax we can only store the integer value inside the list from 0 to 255
name = bytes([3 , 52 , 67 , 123])
print(type(name))
for i in name:
    print(repr(chr(i))) 
# here In the output we can see that everything is correct but why for 3 we are getting '\x03', this is called control character; we can't see control character but we use it mostly which are, "\n" for new line , "\t" for tab, "\b" for backspace , and so on. They control devices, not displayed symbols 
# and here we can see two built-in functions which are repr() and chr() 
# repr() returns a string that shows the exact internal representation of an object, think like you are asking to show me what actually python sees
# chr() it converts unicode integer into its corresponding character



# SYNTAX 3 bytes() "bytes constructor" using string to bytes using encoding
# in this syntax we store the string and represents its unicode after the string
string_bytes = bytes("what is your name" , "utf-8")
print(string_bytes , type(string_bytes))




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# Now we will see one common confusion, and clear it with a small example
zeros = bytes(432)
print(zeros , type(zeros), sep="\n")
# Now we can get confused earlier we studied that bytes only support values from 0 to 255 then why it accepts 432 and gives output also
# first of all bytes() has multiple syntax, which used to store values in bytes using list and string , But this syntax is used to allocating memory of the size but it doesn't store the number
# Here it doesn't store value 432, but it creates a bytes object of length 432 filled with zeros; which means we are allocating memory and using it but the memory is filled with defalut value (zeros). So that why we get output something like '\x00' 432 times