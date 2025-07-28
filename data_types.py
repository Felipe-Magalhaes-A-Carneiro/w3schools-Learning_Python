# Python gas the following data types built-in bu default, in these categories:

# Text Type: str 
# Numeric Types: int, float, complex 
# Sequence Types: list, tuple, range 
# Mapping Type: dict 
# Set Types: set, frozenset 
# Boolean Type: bool 
# Binary Types: bytes, bytearray, memoryview 
# None Type: NoneType 

# remember: you can get the data type of any object by using the 'type()' funcion!

# Text Type: 
# str 
x = 'Hello, Word!'
print("The variable 'x' is igual to" ,x)
print("and your data type is", type(x))
#----

# Numeric Types: 
# int
x = 5
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# float
x = 20.5
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# complex
x = 3j
y = x + 2
print("but now, 'x' is igual to" , x, "so the result with", y, "is", y.real, "to 'real' and", y.imag, "to imag")
print("and your data type is", type(x))
#----

# Sequence Types: 
# list
x = ["apple", "banana", "cherry"]
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# tuple
x = ("apple", "banana", "cherry")
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# range
for x in range(0, 6):
    print(x)

print("but now, 'x' is igual to" , x)
print("and using data type 'range' is", type(x))
#----

# Mapping Type: 
# dict
y = {"name": "Felipe", "age": 32}
print("but now, 'y' is igual to" , y , "and the name is" , y["name"], "than age is" , y["age"], "years old")
print("and your data type is", type(y))
#----

# Set Types: 
# set
x = {"apple", "banana", "cherry"}
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# frozenset
x = frozenset({"apple", "banana", "cherrey"})
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# Boolean Type: 
# bool
x = True
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# Binary Types: 
# bytes
x = b"Hello"
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# bytearray 
x = bytearray(5)
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# memoryview 
x = memoryview(bytes(5))
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# None Type: 
# NoneType
x = None 
print("but now, 'x' is igual to" , x)
print("and your data type is", type(x))
#----

# I can specify the data type, if I whant so