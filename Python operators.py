''' There are 7 types of Operators
*Arithmetic operator
*Assignment operator
*Comparison operator
*Logical operator
*Identity operator
*Membership operator
*Bitwise operator '''

''' Arithmetic operator :
Python Arithmetic operators are used to perform basic math operations, which include addtion, subtraction, and so on.
The various operators Subtraction, Division, Addtion, Multiplication, Floor Division, Exponent and Modulus. '''

# Arithmatic operators are used with numeric values to perform common mathematical operators:

# examples for arithmatic operators

internal_marks = 15
external_marks = 82
number_of_subject = 5
print(internal_marks + external_marks)  # Addtion
print(internal_marks - external_marks)  # Subtraction
print(internal_marks * external_marks)  # Multipliaction
print(internal_marks / external_marks)  # Division

print(internal_marks % external_marks)  # Modulus
print(internal_marks ** external_marks) # Exponentiation
print(internal_marks // external_marks) # Floor Division

''' Assignment operators :
Python Assignment Operators are used to assgin values to the variables. Various operators are +=, -=, *=, /=, etc. '''

# Assignment operators are used to assign values to variables

# Code examples

# Assign: this operator is used to assign the value of the right side of the expression to the left side operator.
internal_marks = 15
print(internal_marks)

# Add and Assign: This operator is used to add the right side operand with the left side operand and then assigning the result to the left operand.
internal_marks =+5
print(internal_marks)

a = 3
b = 5

# a = a + b
a += b
print(a)

# Subtract and Assign : This operator is used to subtract the right operand from the left operand and then assigning the result to the left operand.
internal_marks =-3
print(internal_marks)

a = 8
b = 12

# a = a - b
a-=b
print(a)

# Mutiply and Assign : This operator is used to multiply the right operand with the left operand and then assigning the result to the left operand.
internal_marks *=5
print(internal_marks)

a = 9
b = 10

# a = a * b
a *= b 
print(a)

# Divide and Assign : This operator is used to divide the left operand with the right operand and then assigning the result to the left operand.

a = 6
b = 7

# a = a / b
a /= b
print(a)

# Modulus and Assign : This operator is used to take modulus using the left and the right operands and then aasigning the result to the left operand.

a = 4
b = 6

# a = a % b
a %= b
print(a)

# Divide (Floor) and Assign : This operator is used to divide the left operand with the right operand and then assigning the result(floor) to the left operand.

internal_marks //= 5 
print(internal_marks)

a = 5
b = 8

# a = a //= b
a //= b
print(a)

# Exponent

a = 5
b = 8

# a = a **= b
a **= b
print(a)


''' Comparison operator :-
Comparison operators are used to compare the two values : 
The comparison operators are also called as relational operator. these operators are used to compare the values and return
'True' or 'False' based on the condition. '''
""" Equal to '= =', Greater than or equal to '>=', Greater than '>', Not equal to '!=', Less than or equal to '<=', Less than '<' """

# == Equal to = If the values of two operands are equal, then the condition becomes true. example (a==b)is not true.
# != If values of two operands are not equal, then condition becomes true. example (a!=b)is true.
# > If the value of left operand is greater than the value of right operand, then condition becomes true. eg: (a>b)is not true.
# < If the value of left operand is less than the value of right operand, then condition becomes true. eg: (a<b)is true.
# >= if the value of left operand is greater than or equal to the value of right operand, then condition becomes true. eg: (a>=b)is not true.
# <= If the value of left operand is less than or equal to the value of right operand, then condition becomes true. eg: (a<=b)is true.

