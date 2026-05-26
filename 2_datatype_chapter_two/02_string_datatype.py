#in this section we are going to learn about string from basics to scratch

# A string is a sequence of character used to textual data

example = "vgdg GDS ^&^GG766676jh bhjghU677b" 
print(example)

#basically everything inside quotes is considered as a string which are mentioned below
#letter
#symbol
#number
#whitespace character
#unicode character
#string can be written inside a singel quotes , double quotes and triple quotes but basically we prefer to write inside the double quotes and triple quotes us used for different purpose we will see below in this session

#for example
print("\u0073")
print("\U0001F923")
print("ビジェイ")
print("🥶")

# lets get some basic understanding
print('1+2*3')
print("1+2*3")  # here it will print as it is writtin inside the print statement because we used enclosed the value inside quotes, so python will consider it as a string

print(1+2*3)    # in this statement it will give output as 7(it will calculate according to BODMAS rule) 



# even through we use single quotes(') OR double quotes(") both are used to enclose string value
# for example

create1 = "PYTHON" # here we used single quotes
create2 = 'PYTHON' # here we used double quotes
print(create1 == create2) # here we got output as true because even through we write same string value inside single and double quotes we will get



# now we can think that why python has given the flexibility to use single quotes or double quotes to enclose the string
# we will understant with an example
# imagine I want to write a sentence which is : Don't you know who am I

# will = 'Don't you know who am I' 
# sill = "create " an object" as it is "
# print(sill)
# print (will) here python will count the first two single quotes as a string and will throw an error to complete the last single quotes so here we use double quotes 
# correct version is 

will = "Don't you know who am I"
sill = 'create " an object" as it is '
print(will)
print(sill)

# and some guys will get itch in their ass that they will use single quotes in this sentence : 'you're very creative mr asshole'
# they can use single quotes in this sentence , you can ask how it can be, there are some rules which is called as escape sequence 
# in this rule we use back slash(\) before the quote to tell python that you leave this quote and check for another one 
# for example

prick = 'you\'re very creative mr asshole' # here \ is working as escape sequence
print(prick)

# Now we will see why we use triple quotes 
# triple quotes us used to write multiline string, lets see with an example
multi_line_string = """All the world's a stage,
And all the men and women merely players;
They have their exits and their entrances,
And one man in his time plays many parts,
His acts being seven ages. At first, the infant,
Mewling and puking in the nurse's arms.
Then the whining schoolboy, with his satchel
And shining morning face, creeping like snail
Unwillingly to school"""
print(multi_line_string)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Now we will see string indexing topic  
# indexing is used to access individual characters or substrings using their position within square bracket
language = "JAVA"
#  J      A      V      A 
# [0]    [1]    [2]    [3]   <-- Position/indices for positive numbers
# [-4]   [-3]   [-2]   [-1]  <-- Position/indices for negative numbers
print(language[0],language[2])    # here we used indices to get the particular character and the indices starts from number [0]
#now we will see what happen if we give negative index number
print(language[-1] , language[-3])  # here we seen that if we give [-1] indices it gives last letter 
# note we want to always keep in mind that if we use positive indices than it should start with 0 , and If we use negative indices than we want to start from -1


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Now we will see string slicing topic
# String slicing in python is a way to get the specific parts of a string by using indexes, It contains start, end and step value. which is especially useful for text manipulation and data parsing
# the String slicing syntax is written below
''' 
 string[start : stop : step] 
     here start = index to begin (include)
          stop  = index to end (exclude)
          step  = jump count (optional)
'''
# some examples of slicing
slice_a = "CHRISTOPHER"
#   C     H     R     I     S     T     O     P     H     E      R
#   0     1     2     3     4     5     6     7     8     9     10    <-- positive indices 
#  -11   -10   -9    -8    -7    -6    -5    -4    -3    -2     -1    <-- negative indices
print(slice_a[1:6]) # here the start value is 1 and end value is 6 , always note that the start index value will be printed and the end index value which is mentioned will be exclude which means it will not be printed
print(slice_a[:5]) # here the start value is not mentioned so it will start with beginning and end with 5th index value which will not be printed
print(slice_a[3:]) # here the end value is not mentioned and the start value is mentioned, so here from 3rd index value the output be printed till end
print(slice_a[:]) # here neither the start value is mentioned nor the end value is mentioned so the whole string will be printed
print(slice_a[-9:6]) # here the start value is -9 and the end value is 6, so at start the negative indices is taken and at the end the posive 6 indices is taken
print(slice_a[3:-11]) # now we want to print in reverse order so I have given the start indices 3 and the end indices as -11 , so why we are not getting any output, that we will see below
# now we will learn how to use step value
print(slice_a[3:-11:-1]) # so to print any value in reverse we want to use step as -1
print(slice_a[::-1]) # to print the whole string in reverse
print(slice_a[1:7:2]) #   | --->| --->|     here we can see how the step working by seeing the arrow , here the line shows that the value is printed
                      #  H  R  I  S  T  O     here we used the step count 2, the it will count 2 next value from the current value and will print the second value , then it will take next 2 value and will print the second value
# always remember
#   If start > stop and step is positive → result is an empty string and
#   If start < stop and step is negative → result is an empty string and


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# string concatenation

first_name = "Kiki"
last_name = "MInaj"
print(first_name + " " + last_name)

# string repetition

message = "hi"
print(message * 3) 
# or we can directly print without creating variables
print("hi" * 3)


# now we will learn to check the length of the string
length_a = "Angela White"
print(len(length_a)) # note that the len() funtion also counts the space inside the double quotes


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# COMMON STRING METHODS
# case conversion
case_a = "Alyx Star is great well known actor"
print(case_a.lower()) # it is used to convert the whole string into lower-case
print(case_a.upper()) # it is used to convert the whole string into upper-case
print(case_a.title()) # it is used to convert the first letter of every word in the string from lower-case to upper-case
print(case_a.capitalize()) # it is used to convert the first letter of the first word in the string from lower-case to upper-case

# Removing spaces
space_a = "  Vinland  "
space_b = "Saga"
print(space_a.strip(), space_b) # it is used to remove space from both side
print(space_a.lstrip(), space_b) # it is used to remove space only from left side
print(space_a.rstrip(), space_b) # it is used to remove space only from right side

# Searching
search_a = "quality assurance and quality control with progress and patience"
print(search_a.count("quality")) # it counts that given string is occuring in the whole string
print(search_a.find("and")) # it find where the given string is present in the whole string and returns the output in index number
print("control" in search_a) # it checks whether the given string is present in inside the whole string, if the string is present then it will return true otherwise it will return false

# replace 
r = "do or die"
print(r.replace("or" , "and")) # it is used to replace a particular word in a string

# splitting
splitting = "one,two,three"
print(splitting.split(",")) # it is used to divide the string into parts and store those part in a list
# above we can see that "," (comma) is the seperator , python looks for comma in the string, every time it finds a comma it cuts the string at that point , and returns all the element in list 

# joining
state = ["NewYork" , "New Jersey" , "Utha"]
print(",".join(state))  # it is used to combine elements of a list into a single string
# note that it will only work with string datatype


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# string formatting
name = "Vijay Gunashekaran"
age = 20
place = "Mumbai"
hobbies = "Nothing"

# format() method
print("My name is {} and I am {} years old, I live in {} and I love to do {}".format(name , age , place , hobbies))
# this method is also used in string formatting

# f-string 
print(f"My name is {name} and I am {age} years old, I live in {place} and I love to do {hobbies}")
# the above string formmating is known as f-string which is most commonly used because it is clean and easy to write and understand


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# String comparision

print("stoner" == "stoner")
print("stoner" == "Stoner")
print("a" < "b")
# python string comparision is ascii unicode based
# to check the ascii format we use the below format which is ord() function, it is built-in function 
print(ord("a"))
print(ord("b"))

