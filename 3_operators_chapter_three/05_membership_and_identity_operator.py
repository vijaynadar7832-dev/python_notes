# Membership Operator
# membership operator is used to check whether a value exists inside a sequence

"""
there are only two membership operators:
operators                        meaning
    in                 returns True if value is present, and returns False if value is NOT present
  not in               returns True if value is NOT present, and returns True if value is present
"""

# Example with list
mem_list = [32 , False , "routing" , 62]
print(True in mem_list)
print("route" not in mem_list)
print("\n")

# Example with string
mem_string = "complicated"
print("l" in mem_string)
print("il" not in mem_string)
print("\n")

# Example with tuple
mem_tuple = (62 , 7 , "rotten")
print(62 in mem_tuple)
print("rotten" not in mem_tuple)
print("\n")

# Example with dictionary
# in dictionary membership checks keys NOT values
mem_dict = {"name" : "stake" , "age" : 32}
print("name" in mem_dict)
print(32 in mem_dict)
print(32 not in mem_dict)
print("\n")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Identity Operator
# identity operator checks whether two variables are actually of same datatype and share same memory location ; identity operator is not same as (==) operator

# example 1
first_iden = 233
second_iden = 233
print(first_iden is second_iden)
print(first_iden is not second_iden)
print(id(first_iden) , id(second_iden)) # here you can see both object points to same memory address
print("\n")

# example 2
list_1 = [1,2,3]
list_2 = [1,2,3]
print(list_1 is list_2)
print("\n")

# NOTE = now here you can get doubt in integer why the object is pointing to same memory address when the integer are same , and in list why different object's are created even through both the list are same
# because integer is immutable, so for memory optimization it reuses memory , but in list it is mutable so python creates a new  object every time (unless you explicitly assign reference)

# example 3
lis_1 = [1,2,3]
lis_2 = lis_1
print(lis_1 is lis_2) 