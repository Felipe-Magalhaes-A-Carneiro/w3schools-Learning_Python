# Python has a set of built-in methods that can use on strings.

#UPPER CASE:
a = "Hello, Word!"
print(a.upper())

# LOWER CASE:
print(a.lower())

#------------

# REMOVE WHITESPACE
#Whitespace is the space before and/or after actual text, and very often you want to remove this space

b = " Hello, Word! "
print(b.strip())

#-----

# REPLACE STRING
# The 'replace()' method replaces a string with another string:

print(a.replace("H", "J"))

#-----

# SPLIT STRING
# The 'split()' method returns a LIST where the text between the specified separator becomes the list items

print(a.split(","))

#-----
