# In Python, variables are created when you assign a value to it:
x = 5
y = "Hello, Word!"

print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4
print(x)

x = "Now x is a string!"
print(x)

# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)
y = int(3)
z = float(3)

print(x, y, z)

# also, you can get the data type of a variable with the type() funciton:

x = 5
y = "Hello, Word!"

print(type(x))
print(type(y))

# Case-sensitive => Variables names are case-sensitives!

a = 32
A = "Felipe"
# A will not overwrite a
print(A, a)