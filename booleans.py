# Booleans represent one of two values: 'True' or 'False'

# You can evaluate any expression in Python, and get one of two answers, 'True' or 'False'.

print(10 > 7) # True
print(10 == 25) # False

# When you run a 'condition' in an 'if', statement, Python returns True or False

a = 200
b = 33

if a > b:
    print("a is greater than b")
else:
    print("b is not greater than a")

# EVALUATE VALUE AND VARIABLES

# The 'bool()' function allows you to evaluate any value, and give you 'True' or 'False' in return

print(bool("Hello"))
print(bool(15))

# MOST VALUES ARE TRUE

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.
print(bool("Hello"))
print(bool(""))
# Any number is True, except 0.
print(bool(15))
print(bool(0))

# Any list, tuple, set, and dictionary are True, except empty ones.

# tuple
bool(())

# List
bool([])

# dict
bool({})

# One more value, or object in this case, evaluates to 'False', and that is if you have an object that is made from a class with a '__len__' function that returns '0' or 'False':

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))


# FUNCTION CAN RETURN A BOOLEAN

def myFunction():
    return True

print(myFunction())


# you can execute code based on the Boolean answer of a function
def myNewFunction():
    return True

if myNewFunction():
    print("YES!")
else: 
    print(("NO!"))

# BUILT-IN
# isinstance(), can be used to determine if an object of a certain data type

x = 200
print(isinstance(x, int))