# # numbers = [10,20,3,5,100]
# # x = bytearray(numbers) # bytearray
# # print(x)
# # print(len(x))
# y = memoryview(bytes(5))
# print = (y) 
# y = memoryview(bytearray(0))
# print = (y)

# # import keyword
# # print(keyword.kwlist)
# # print(len(keyword.kwlist))

byte_array = bytearray('1XYZ', 'utf-8')

mv = memoryview(byte_array)

print(mv[0])
print(bytes(mv[0:1]))
