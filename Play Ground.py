# # # numbers = [10,20,3,5,100]
# # # x = bytearray(numbers) # bytearray
# # # print(x)
# # # print(len(x))
# # y = memoryview(bytes(5))
# # print = (y) 
# # y = memoryview(bytearray(0))
# # print = (y)

# # # import keyword
# # # print(keyword.kwlist)
# # # print(len(keyword.kwlist))

# # byte_array = bytearray('1XYZ', 'utf-8')

# # mv = memoryview(byte_array)

# # print(mv[0])
# # print(bytes(mv[0:1]))

# internal_marks = 15
# external_marks = 82
# number_of_subject = 5
# # print(internal_marks + external_marks)  # Addtion
# # print(internal_marks - external_marks)  # Subtraction
# # print(internal_marks * external_marks)  # Multipliaction
# # print(internal_marks / external_marks)  # Division

# print(internal_marks % external_marks)  # Modulus
# print(internal_marks ** external_marks) # Exponentiation
# print(internal_marks // external_marks) # Floor Division

# a = 458
# b = 548

# # a = a + b
# a += b
# print(a)

# x = "1" + 2
# print(x)

def my_function():
	'''Demonstrates triple double quotes
	docstrings and does nothing really.'''

	.return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)
