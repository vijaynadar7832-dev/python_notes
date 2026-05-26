# range is a built-in immutable sequence datatype in python used to represent a sequence of integers defined by a start, stop, and step , and range dosen't store the numbers in the memory
# And range doesn't store the numbers in the memory, which means, range doesn't keep all the numbers in the memory(RAM) , instead it only remembers that how to calculate them
# So we can understand like this , range saves memory by storing only the start, stop, and step and calculates each value only when needed
# if you still don't understand about the memory concept , think if you want to store 1 million numbers in list then the list will store the numbers in the memory , on other hand if we store 1 million numbers in range then it store only in 3 values start , stop and step ; thats why range is fast and memory-friendly 
# range only accepts integer values

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Now we will learn how to write range , there are three syntax for range , we will understand each and how to execute.
""" In range only 3 values are used:
    start = start value it's default value is 0 which means if no value is inserted in the range then it will start with 0 number and start value is optional , if we enter any value it will be included
    stop = end value it's mandatory value and we cannot keep it blank , whatever value is inserted in the stop it will be excluded which means till it's previous value is included eg :- I want to print till 100 so I want to enter 101
    step = it decides how many numbers to jump each time, it's default value is 1 which mean if no value is insert it will not skip values and it is optional """

""" range(31) = (stop) "here the value is stop value"
    range(3 , 31) = (start , stop) "here the first value is start and second value is stop"
    range(1 , 51 , 2) = (start , stop , step) "here the first value is start , second is stop and third is step" """ 

# BASIC_SYNTAX
basic_syntax = range(1 , 21)
print(basic_syntax) 
# when we directly print the range then we will get output as range(1, 21) , now we can think that what the fuck is this why it doesn't print the list of numbers from 1 to 20
# when we directly print the range then it only displays the start and stop value as same; it's basically saying "I know how to generate numbers from 1 up to 20, but I won't generate them unless you ask"; that why range is also called as memory efficient and lazy(numbers are produced when needed)
# so now we can ask that how the actually see the numbers, by using typecastin , unpacking and using for loop , so now we will see each.

# unpacking operator ( * )
print(*basic_syntax) # here the unpacking operator is used to unpack the range object and send each value seperately to print() , internally it still iterates but we didn't write a loop

# list 
print(list(basic_syntax)) # here we are converting it first to list datatype, and it is mutable

# tuple
print(tuple(basic_syntax)) # here we are converting it first to tuple datatype , it is similar to list but it is immutable

# set 
print(set(basic_syntax)) # here we are converting it first to set datatype , use this if order doesn't matter, and it is mutable 

# for loop
for i in basic_syntax:
    print(i)
print("DONE!")  # in this for loop prints the value one-by-one
print("\n")



# SYNTAX 1
range_syntax_1 = range(21)
print("syntax 1")
for i in range_syntax_1:
    print(i)
# in this syntax we are only defining the end value because it is mandatory in range, and the stop value is -1 of the mentioned value in the range 
print("\n")



# SYNTAX 2
range_syntax_2 = range(11 , 36)
print("syntax 2")
for i in range_syntax_2:
    print(i)
# in this syntax we are defining both the start value and stop value, here we mentioned the start value because we want to start the value other than the default value which is 0
print("\n")



# SYNTAX 3
range_syntax_3 = range(1 , 41 , 3)  
print("syntax 3")
for i in range_syntax_3:
    print(i)
# in this syntax we are defining all the 3 values which is start , stop, and step value , step value defines that how much number to jump each time
print("\n")



# here we will see how range datatype is immutable
# range_immutable = range(1 , 21)
# range_immutable[3] = 3
# print(list(range_immutable))
# print("\n")
# if you comment out and run the above code it will give you error by changing in the same memory object

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# indexing in range
range_index = range(1 , 21)
print(range_index[1])
print("\n")

# slicing in range
range_slicing = range(1 , 11)
print(list(range_slicing[2:7]))
print("\n")

# negative range
neg_range = range(10 , 0 , -1) # Always remember that if you want to print in reverse order , then in start mention the number from where you want to print in reverse , then mention the number in stop till where you want to stop in reverse , and always use the -1 in step to reverse
for i in neg_range:
    print(i)
# if you also want to print the 0 number at the reverse just add -1 in stop value
print("\n")


# checking membership (in)
mem_range = range(1 , 11 , 2)
print(3 in mem_range)
print(8 in mem_range)
# the membership is used to check whether the given number is present in range or not , if the value is present the it will print True if not present the it will print False
print("\n")


# range length 
length_range = range(1 , 11)
print(len(length_range))