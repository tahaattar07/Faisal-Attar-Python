 
# PYTHON PROGRAM: ALL BUILT-IN DATA TYPES
print("\n INTEGER (int)")
a = 100
print(a)
print(type(a))
 
print("\n FLOAT (float)")
b = 10.75
print(b)
print(type(b)) 
print("\n COMPLEX (complex)")
c = 5 + 3j
print(c)
print(type(c))
print("\n BOOLEAN (bool)")
d = True
e = False
print(d)
print(e)
print(type(d)) 
print("\n STRING (str)")
name = "Faisu"
print(name)
print(type(name)) 
print("\n LIST ")
my_list = [10, 20, 30, "Python", 5.5]
print(my_list)
print(type(my_list)) 
print("\n TUPLE")
my_tuple = (1, 2, 3, "Hello", 7.5)
print(my_tuple)
print(type(my_tuple)) 
print("\n RANGE")
r = range(1, 6)
print(list(r))
print(type(r))

print("\n DICTIONARY (dict) ")
student = {
    "Name": "Faisal Attar",
    "Age": 19,
    "City": "Pune"
}
print(student)
print(type(student))

print("\n SET ")
my_set = {10, 20, 30, 40}
print(my_set)
print(type(my_set))

print("\n FROZENSET ")
fs = frozenset([1, 2, 3, 4])
print(fs)
print(type(fs))

print("\n BYTES ")
byte_data = bytes([65, 66, 67, 68])
print(byte_data)
print(type(byte_data))

print("\n BYTEARRAY")
byte_array = bytearray([65, 66, 67, 68])
print(byte_array)
print(type(byte_array))


print("\n NONE TYPE")
x = None
print(x)
print(type(x))

