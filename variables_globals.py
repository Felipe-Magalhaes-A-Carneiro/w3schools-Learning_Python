# Variables that are created outside of a funcion (as in all of the examples in the previous documments) are known as global variables.

# Global variables can be used by everyone, both inside of funcition and outside

x = "awesome!"

def myfunc():
    print("Python is " + x)

myfunc()

# the variable created inside the function it is called local, ande can only be used inside the function

def myfunc2():
    x = "fantastic!"
    print("Python is " + x)

myfunc2()

# but, if you whant to create a variable thats is local and be used by everyone, you can use the keyword 'global':

def myfunc3():
    global y 
    y = "eazy!"

myfunc3()

print("Python is " + y)

a = "nice!"

def myfunc4():
    global a
    a = "eazy!"

myfunc4()

print("Python is " + a)