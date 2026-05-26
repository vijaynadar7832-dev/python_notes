# bytearray datatype is very similar to bytes datatype, but there is one major difference between these two datatypes are bytes datatype is immutable and bytearray is mutable datatype
# so all the other basic concepts except mutable and immutable are same in bytes datatype , just go and refer the bytes_datatype.py file in chapter two
# because bytearray datatype is mutable it add some more modify functions like extend() , insert() , append() , etc.
""" Now we we will see why we need bytearray datatype if we already have bytes datatype to work with raw binary data? 
    - Imagine you are working with network packets , file data , images , encryption tool ; sometimes you must need to change raw binary data, in this case if you use bytes datatype python will not allow you to perform modification, that's why we use bytearray datatype here python allows you to perform modification in raw binary data 
"""

# Now we will see how bytearray is mutable
mutable_bytearray = bytearray([38 , 23 , 243 , 23])
print(mutable_bytearray)
mutable_bytearray[0] = 255
print(mutable_bytearray , type(mutable_bytearray))
print("\n")



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Now we will see different syntax of bytearray datatype below

# SYNTAX 1 (empty bytearray)
empty_bytearray = bytearray()
print(empty_bytearray)
# In this we can create an empty mutable binary object

# SYNTAX 2 (using size - memory allocation)
allocation_bytearray = bytearray(34)
print(allocation_bytearray)
# in this python allocates 34 bytes filled with zeros
# this is used to allocate reserve memory space to use it later

# SYNTAX 3 (using list [ ] )
list_bytearray = bytearray([23 , 64 , 73 , 234])
for i in list_bytearray:
    print(repr(chr(i)))
# we can only store values from 0 to 255 
# repr() returns a string that shows the exact internal representation of an object, think like you are asking to show me what actually python sees
# chr() it converts unicode integer into its corresponding character

# SYNTAX 4 (string, using encoding)
string_bytearray = bytearray("Bhurj Khalifa" , "utf-8")
print(string_bytearray)
# in this python encodes each character into bytes using utf-8 encoding
print("\n")



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Now we will see some functions in bytearray to perform modification

# .append()
append_bytearray = bytearray([73 , 62 , 63 , 87])
print(append_bytearray)
append_bytearray.append(71)
print(append_bytearray)
print("\n")

# .insert()
insert_bytearray = bytearray([73 , 62 , 63 , 87])
print(insert_bytearray)
insert_bytearray.insert(3,53)
print(insert_bytearray)
print("\n")

# .extend()
extend_bytearray = bytearray([73 , 62 , 63 , 87])
print(extend_bytearray)
extend_bytearray.extend([67 , 123 , 233])
print(extend_bytearray)

# .reverse()
sort_bytearray = bytearray([73 , 62 , 63 , 87])
print(sort_bytearray)
sort_bytearray.reverse()
print(sort_bytearray)
# now we can think if we can use .reverse() then why can't we do .sort() 
# bytearray is not a list datatype it is used to store the values in raw binary so sometimes we need the raw binary data in reverse order , but not to destroy the original structure, so that's why .sort() is not allowed in bytearray
# and sorting could also destroy packet structure, corrupt encrypted data and break file format
print("\n")

# .pop()
pop_bytearray = bytearray([73 , 62 , 63 , 87])
print(pop_bytearray)
pop_bytearray.pop(2)
print(pop_bytearray)


# we can also do slicing and indexing in both bytes datatype and bytearray datatype


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# now we will see conversion between bytes and bytearray and vice-versa

# bytes ----> bytearray
bytes_datatype = bytes([23 , 52 , 34])
print(bytes_datatype , type(bytes_datatype))
to_bytearray = bytearray(bytes_datatype)
print(to_bytearray , type(to_bytearray))
print("\n")

# bytearray ----> bytes
bytearray_datatype = bytearray([23 , 52 , 34])
print(bytearray_datatype , type(bytearray_datatype))
to_bytes = bytes(bytearray_datatype)
print(to_bytes , type(to_bytes))


# NOTE = Always remember that bytes and bytearray do not store characters. They store integers (0–255), and each integer is represented internally in memory as an 8-bit binary value (1 byte). For example, 01010101 represents one byte
# NOTE = this is how bytes and bytearray encoding works; # Character → Unicode code point → UTF-8 encoding → bytes → binary in RAM