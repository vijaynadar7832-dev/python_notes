# NOW WE ARE GOING TO LEARN ABOUT VARIOUS TYPES OF COPY AND COPY METHOD IN DETAIL, SO LET'S START


# ORIGINAL TYPE OF COPY
list_original = [1,2,3,4]
list_duplicate = list_original
print(list_original , id(list_original))
print(list_duplicate , id(list_duplicate))
list_original.extend([5,6,7])
list_duplicate.append(8)
print(list_original , id(list_original))
print(list_duplicate , id(list_duplicate))
# In this type of copy we have seen that both the object are refering to the same memory address and it creates a problem which is, If we try to modify one object then if will affect another object also
# So it means if we use assignment equal operator then both the object will refere to same memory address, and if we change one object then It will affect other object
print("\n")
print("\n")
print("\n")






# NOW TO USE SHALLOW COPY AND DEEP COPY WE WANT TO IMPORT COPY MODULE, WE CAN USE SHALLOW COPY WITHOUT COPY MODULE BUT WE MUST NEED COPY MODULE FOR DEEP COPY
import copy





# SHALLOW COPY
original_shallow = [1,2,3,4]
duplicate_shallow = copy.copy(original_shallow)
print(original_shallow , id(original_shallow))
print(duplicate_shallow , id(duplicate_shallow))
original_shallow.append(5)
duplicate_shallow.clear()
duplicate_shallow.extend([6,7,8,9])
print(original_shallow , id(original_shallow))
print(duplicate_shallow , id(duplicate_shallow)) 
print("\n")
# here python is copying the list and creating a new independent list as original list but both the list are stored in different memory address, due to different memory address if we change one list it will not affect another list
# but here is problem in shallow copy while performing nested list, lets see the example
original_shallow_nested = [1,2,3,4,[1,2,3,4]]
duplicate_shallow_nested = copy.copy(original_shallow_nested)
print(original_shallow_nested , id(original_shallow_nested))
print(duplicate_shallow_nested , id(duplicate_shallow_nested))
original_shallow_nested[4].append(5)
duplicate_shallow_nested[4].extend([6,7,8])
print(original_shallow_nested , id(original_shallow_nested))
print(duplicate_shallow_nested , id(duplicate_shallow_nested))
# here we can see that in shallow copy the top level list has only independent memory address but the inner level list which is nested list has shared memory address 
# to tackle this problem there is deep copy which we will see below
print("\n")
print("\n")
print("\n")






# DEEP COPY
original_deep = [1,2,3,4]
duplicate_deep = copy.deepcopy(original_deep)
print(original_deep , id(original_deep))
print(duplicate_deep , id(duplicate_deep))
duplicate_deep.insert(4,5)
print(duplicate_deep)
print(original_deep) 
# here we are changing the copy but the original remains same which means deep copy creates independent memory address to the copy list also
# now we will try with nested list
print("\n")
original_deep_nested = [1,2,3,[1,2,3]]
duplicate_deep_nested = copy.deepcopy(original_deep_nested)
print(original_deep_nested , id(original_deep_nested))
print(duplicate_deep_nested , id(duplicate_deep_nested))
original_deep_nested[3].append(4)
duplicate_deep_nested[3].append(55)
print(original_deep_nested , id(original_deep_nested))
print(duplicate_deep_nested , id(duplicate_deep_nested))
# here we can see that the nested list also independent, which means if we change original nested list it will not affect the copied list, so here we can see that the nested list also refering the unique memory address in deep copy
print("\n")
print("\n")
print("\n")


# Now using the IS operator we will check each copy method
original = [[1,3],
            [3,4]]

copy1 = original
print(f"same object? : {original is copy1}  ""\n")

copy2 = copy.copy(original)
print(f"same object? : {original is copy2}  ")
print(f"same list? : {original[0] is copy2[0]}  ""\n")

copy3 = copy.deepcopy(original)
print(f"same object? : {original is copy3}  ")
print(f"same list? : {original[0] is copy3[0]}  ""\n")