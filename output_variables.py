# the function print() is a good example about what is a output

x = "Python is awesome."
print(x)

# in this fuction, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome. "
print(x, y, z)

# but you can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome. "
print(x + y + z)

# Notice the space character after "Python " and "is ", this is necessary compared to using a comma

# For numbers, the + character works as a mathematical operator:

a = 5
b = 3
print(a + b)

# WARNING: If you use + to combine a string and a number, Python will give you an error:

#c = 9
#d = "test"
#print(c + d)

# to fix this, use comma ' , '