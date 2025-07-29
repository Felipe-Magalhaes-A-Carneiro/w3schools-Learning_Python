# There are three numeric types in Python:
 
# int (integer) = is a whole number, positive or negative, without decimals, of unlimited length
a = 5
b = 3546984565563
c = -35484612
print(type(a))
print(type(b))
print(type(c))

#---------

# float (float point number) = is a number, positive or negative, containg one or more dicimals 
d = 2.8
e = 1.10
f = -35.59
print(type(d))
print(type(e))
print(type(f))

# float can be also scientific numeric with an "e" to indicate the power of 10
d = 2e8
e = 1e10
f = -35e59
print(type(d))
print(type(e))
print(type(f))

#---------

# complex = complex numbers are written a "j" as the imaginary part
g = 1j
h = 5j
i = -5j
print(type(g))
print(type(h))
print(type(i))

#---------

# Type Conversion
# You can convert from one type to another with the int(), float(), complex() methods

x = 1
print(type(x))

y = 2.8
print(type(y))

z = 1j
print(type(z))

# convert from int  to float:
m = float(x)
print(type(m))

# convert from float  to int:
n = int(y)
print(type(n))

# convert from int  to complex:
o = complex(x)
print(type(o))

# Note: You cannot convert complex numbers into another numbert type!

# Random Number
# Python does not have a random() function, but Python has a built-in module called 'random' tha can be used:

import random

print(random.randrange(1, 10))