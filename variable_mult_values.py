# Python allows you to assing values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Apple"

print(x)
print(y)
print(z)
print(x, y, z)

# and ONE value to multiple variables:

x = y = z = "Apple"

print(x)
print(y)
print(z)
print(x, y, z)

# Unpack a collection:
# You can have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpaking:

fruits = ["apple", "banana", "orange"]

x, y, z = fruits

print(x)
print(y)
print(z)
print(x, y, z)