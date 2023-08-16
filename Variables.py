'''Variables'''

# An integer assignment
age = 45
# A floating point
salary = 1456.8
# A string
name = "John"
# printing statement
print(age)
print(salary)
print(name)

# Re-declare the variable
Number=100
# display
print("Before RE declare:", Number) #"Before RE declare:",
# re-declare the var
Number=120.3
print(Number) #"After re-declare:",

# Assigning different values to multiple variables:
a,b,c = (1,20.2,"Learn Python in Tamil")
print(a)
print(b)
print(c)

# String - is a single, double and triple quote
name = "Data Science"
Name = 'Data Science'
university = """Anna University"""
University = '''Anna University'''

location = '''Anna University is located in chennai'''

print(name) 
print(Name)
print(university) 
print(University)
print(location)


""" Python Data Types
Numeric - Integer , Float, Complex.
Boolean
Set
Mapping (dictionary)
Sequence - String, List and Tuple """

""" x = "Hello Python" #str
x = 21             #int
x = 202.5          #float
x = 3j             #complex
x = True           #bool

x = ["apple", "banana", "cherry"]   #list
x = ("apple", "banana", "cherry")   #tuple
x = {"name" : "John", "age" :36}    #dict
x = {"apple", "banana", "cherry"}   #set
x = ({"apple", "banana", "cherry"}) #frozenset """

# Play Ground
Everyone = "please slient"
print(Everyone)

Love = 25+62.21
print(Love)


# bytearray

x = bytearray(5)
print(x)

numbers = [10,20,3,5]
x = bytearray(numbers)
print(x)

'''
bytearray() Parameters
bytearray() takes three optional parameters:

source (Optional) – source initializes the array of bytes
Depending on the type of source, the bytearray() function follows some specific rules.

* If there is no parameter, an empty byte array is returned.
* If the source is a string, the encoding argument must be used.
* The array will have the same size as the source and will be initialized with null bytes if the source is an integer.
* If the source is a buffer interface object, the bytes array will be initialized with a read-only buffer from the object.
* If the source is an iterable object, the elements must all be integers in the range 0 to 256.
=> encoding (Optional) – If the source is a string, the string’s encoding is returned.
=> errors (Optional) – if the source is a string when encoding fails, it takes action. 
Return value from bytearray()
The bytearray() function returns a byte array with the specified size and initialization settings.
'''

n = "Python"

arr = bytearray(n, 'utf-8')

print(arr)

''' 
What is a Bytearray in Python?
The bytearray() method returns a bytearray object, which is an array of bytes. It returns a mutable series of integers between 0 and 256. 
The source parameter of the ByteArray is used to initialize the array. Such as:

Method 1:

Bytearray() transforms a string to bytes using str.encode() if the encoding and errors parameters are given
'''

str = "Geeksforgeeks"


# Using Unicode 8 and 16 to 

# encode the string

array1 = bytearray(str, 'utf-8')

array2 = bytearray(str, 'utf-16')


print(array1)

print(array2)


''' Method 2:

If the value is an integer, it produces an array of that size with null bytes. '''

size = 3


# will make an array of the #specified size and fill it with null 

# bytes

array1 = bytearray(size)


print(array1)


''' Method 3:

The read-only buffer will be utilized to initialize the bytes array if it is an Object.

Source Code '''

# Bytearray is created from a byte literal

arr1 = bytearray(b"abcd")


#the value being iterated

for value in arr1:

    print(value)


# Create a bytearray object

arr2 = bytearray(b"aaaacccc")


# count bytes from the buffer

print("Count of c is:", arr2.count(b"c"))

''' Method 4: 

If an Iterable(range 0=x 256) is used as the array’s initial contents

Source Code '''

# simple list of integers

list = [1, 2, 3, 4]


# iterable as source

array = bytearray(list)


print(array)

print("Count of bytes:", len(array))

''' Method 5:

If there is no source, a zero-sized array is constructed.

Source Code '''

# There will be a size 0 array formed.

# iterable as source

array = bytearray()

print(array)

''' What is the Difference Between Bytes and bytearray in Python?
The bytes and bytearray classes both feature arrays of bytes with values ranging from 0 to 255 for each byte. 
The main difference is that a bytes object is immutable, which means that once formed, its elements cannot be changed. 
A bytearray object, on the other hand, allows you to change its elements.

Program to append bytes and bytearrays
The ‘+ operator’ can be used to catenate bytes and bytearray objects. Note that the catenated result inherits the first argument’s type, so a+b produces bytes object, 
while b+a produces a bytearray.

Source Code '''


a = bytes(3)

print(a)

b = bytearray(4)

print(b)

print(a+b)

b+a

''' Is Bytearray mutable in python?
Yes, the Bytearray function in Python is mutable. This indicates that the elements of the function can be easily altered. 

For example: '''

b = bytearray('abc', 'UTF-8')

print(b) 

b[1] = 65 # mutable 

print(b)

# Home Work
# TypeError: bytearray() takes at most 3 arguments (4 given)
numbers = [10,20,3,5,100] # [10,20,3,5,1000]
x = bytearray(numbers) # bytearray
print(x)
print(len(x))





