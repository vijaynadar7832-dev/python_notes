# List datatype is used to store multipe values, either of same type or different type with Unique or duplicate values in a single object
# To store the values in the list it should be enclosed inside the square bracket [] and seperated using comma ,
# In list elements are fixed and , order is preserved 

list_a = [12 , -12 , 1.1 , -3.2 , "Public property" , True]
print(list_a)
# this is how we create a list 
# we can add, modify, or remove elements from the list because list is immutable which means we can alter data in same memory address

list_a[1] = 12
print(list_a)

# we can also create a empty list 
empty_list_a = [] # list literal notation
print(empty_list_a)
empty_list_b = list() # list constructor method , it is basically used to convert any datatype to list datatype
print(empty_list_b)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# list indexing
index_list = [3 , 4 , 3.3 , -2.6 , 0.4 , "python" , True]
print(index_list[3]) # indexing through positive number 
print(index_list[-1]) # indexing through negative number

# list slicing
index_slice = [2 , False , "Happy New Year" , 0.33 , "ASAP"]
print(index_slice[1:4])
print(index_slice[::3])

# change element in list
list_change = [3 , 22 , 245 , 134 , 532 , 623 , 713]
list_change[0] = 923 # here we are changing the index value 0 element to another value 
print(list_change) # here we are printing the changed value

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Add elements in the list

# append()
list_append = [323 , 425 , 654 , 735 , 143 , 632]
list_append.append(987) # .append() is used to add element at the end of the list, but in this we can only add one element at the end of the list
print(list_append)

# extend()
list_extend_a = [323 , 425 , 654 , 735 , 143 , 632]
list_extend_b = ["Angela White" , True]
list_extend_a.extend([928 , 283 , 823]) # .extend() is used to enter multiple element at the end of the list
print(list_extend_a)
list_extend_a.extend(list_extend_b) # In .extend() we can also add one list element into another list
print(list_extend_b)
print(list_extend_a)


# insert()
list_insert = [323 , 425 , 654 , 735 , 143 , 632]
list_insert.insert(3 , 111) # here we are inserting a new element in a list at a particular index, .insert(index_no , value)
print(list_insert)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Removing elements from list

# remove()
list_remove = [323 , 425 , 654 , 735 , 143 , 632]
list_remove.remove(425) # remove() is used to remove a particular element from the list using a value
print(list_remove)

# pop()
list_pop = [323 , 425 , 654 , 735 , 143 , 632]
list_pop.pop(3) # pop() is used to remove a particular element from the list using a index number 
print(list_pop)

# clear()
list_clear = [323 , 425 , 654 , 735 , 143 , 632]
list_clear.clear() # clear() is used to remove all element from the list
print(list_clear)



# commonly used list methods

# count()
list_count = [323 , 425 , 654 , 735 , 143 , 632 , 425]
print(list_count.count(425)) # count() is used to count how many similar values are there in the list which is mentioned inside the () bracket

# index()
list_index = [323 , 425 , 654 , 735 , 143 , 632 , 425]
print(list_index.index(425)) # index() is used to find the index number of the element

# sort()
list_sort = [323 , 425 , 654 , 735 , 143 , 632 , 425]
list_sort.sort() # .sort() is used to sort the list in ascending order 
print(list_sort)
list_sort.sort(reverse=True) # .sort(reverse=True) is used to sort the list in descending order
print(list_sort)

# reverse()
list_reverse = [323 , 425 , 654 , 735 , 143 , 632 , 425]
list_reverse.reverse()
print(list_reverse) # reverse() is used to reverse the list in 


# NOTE :- now we can doubt that why we write the clear() , sort() , pop() , remove() , insert() , extend() , append() , reverse() method outside the print statement and we print it seperately and in other hand why we write the index() and  count() method inside the print statement , if we do not follow the rule we get error why?
# NOTE :- now I will expalin in detail the the methods which are written in the first are all action commands which means we are changing the list values and modifying it so we want to write it outside the print statement and print it seperately but the second methods are only used for querying it does not alter or change any value so we want to write the method inside the print statement directly


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nested list
# A list inside another list is known as nested list
list_nested = [ [3 , 4 , 2] , 
                [7 , 3 , 3] , 
                [2 , 6 , 7] ]
print(list_nested[0][2]) # here for a nested list we are doing a simple matrix example of finding the row and column of a matrix  
list_nested[0][1] = 69 # here we are modifying the nested list using the index value the first index value 0 is the outer list element and the second index value 1 is inner list element
print(list_nested)

# del()
list_del = [323 , 425 , 654 , 735 , 143 , 632 , 425]
del(list_del) # clear() data only deletes the elements inside the list but in del() it deletes all object with elements
# print(list_del) # if we try to print this variable then we will get a name error
print("\n")



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# LIST COMBINING

number = [12,43,53]
names = ["star" , "moon"]
number_names = number + names
print(number_names) 
# print(id(number + names)) #
# Here we can see that we combined two list and stored inside another list
# but here we are directly giving the value to the print, then where will the combined list will store, the value inside the print statment will create a temporary new list and will store the combine element inside it and once it is printed as output then it is immediatly discarded by the memory through garbage collector


print(number * 3)
# used to combine the same list multiple times


# combine_nested = [number , names]
print([number , names])
# used to combine both the list and store as a nested list inside a list


letters = ["a" , "b" , "c"]
numb = [1 , 2 , 3]
letters.extend(numb)
print(letters)
# this method is used when we don't want to create a new object to combine a list , in this the letters object will only get extended and combine value will store in the object





# zip() is a built-in Python function that pairs elements from multiple iterables (like lists)
# It pairs:
# first with first
# second with second
# third with third
# and so on…
# If both list length are different then zip() stops at the shortest iterable
# lets see an example
ids = [1,2,3,4]
names_employee = ["sara" , "sabnam" , "alina"]
print(list(zip(ids,names_employee)))
print(zip(ids,names_employee))
# to print zip first we want to convert it into list , otherwise we will get some weird code