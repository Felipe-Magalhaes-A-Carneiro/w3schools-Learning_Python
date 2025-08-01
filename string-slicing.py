# SLICING
# You can return a range of characters, separated by a colon, to return a part of the string

b = "Hello, Word!"
c = "Welcome"
print(c[2:5])

# SLICING FROM THE START:
print(b[:5])

# SLICING TO THE END:
print(b[2:])

# NEGATIVE INDEXING
# Use negative indexes to start the slice from the end of the string:

c = "Welcome"
print(c[-5:-2])