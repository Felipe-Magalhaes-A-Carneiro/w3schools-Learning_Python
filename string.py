# Strings in Python are surronded by either single quotation marks, or double quoatation marks

# 'Hello' is the same as "Hello"
print('Hello')
print("Hello")

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("He is called 'Felipe'")
print('He is called "Felipe"')

# You can assign a multiline string to a variable by using three quotes or three single quotes:

a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua."""

print(a)
#---------

# Strings are Arrays
# In Python, are arrays of unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to acess elements of the string

s = "Hello, Word!"
print(s[1])
#---------

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with for loop.

print("I can spell 'banana':")
for x in "banana":
    print(x)
#---------

# String length
# To get the length of a string, use the len() function

print(len(s))
#---------

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword 'in'.

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")
#---------

# Check if not
print("paid" not in txt)

if "paid" not in txt:
    print("No, 'paid' is not present.")