# Operators 
# Python divides the operators in the following groups:

# Arithmetic operators / aritiméticos
a = 10 + 6
a = 10 - 6
a = 10 * 6
a = 10 / 6
a = 10 % 6
a = 10 ** 6 # exponentiation
a = 10 // 6 # floor division

# Assignment operators / atribuição
# are used to assign values to variables:
b = 10
b += 5 # same as 'b = b + 5'
b -= 5 # same as 'b = b - 5'
b *= 5 # same as 'b = b * 5'
b /= 5 # same as 'b = b / 5'
b %= 5 # same as 'b = b % 5'
b //= 5 # same as 'b = b // 5'
b **= 5 # same as 'b = b ** 5'
b &= 5 # same as 'b = b & 5'
b |= 5 # same as 'b = b | 5'
b ^= 5 # same as 'b = b ^ 5'
b >>= 5 # same as 'b = b >> 5'
b <<= 5 # same as 'b = b << 5'
# b := 5 # same as 'b = 5 print(b)'

#Comparison operators / comparação
# are used to compare two values (NOTE: The answear always will be True or False):
c = 0
c == 5 # Equal
c != 5 # Not equal
c > 5 # Greater than
c < 5 # Less than
c >= 5 # Greater than or equal to
c <= 5 # Less than or equal to


#Logical operators
# are used to combine conditional statements:

c < 5 and b < 10 # Returns True if both variables are the same object
c < 5 or b < 10 # Returns True if both variables are not the same object
not (c < 5 and b < 10)

#Identity operators
# are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

a is b # Returns True if a sequence with the specified value is present in the object
a is not b # Returns True if a sequence with the specified value is not present in the object

#Membership operators
# are used to compare the objects, not if they  are equal, but if they are actually the same object, with the same memory location:

a in b # Returns True if a sequence with the specified value is present in the object
a not in b # Returns True if a sequence with the specified value is not present in the object

#Bitwise operators
# are used to compare (binary) numbers:

b & c # Sets each bit to 1 if both bits are 1
b | c # Sets each bit to 1 if one of two bits is 1
b ^ c # Sets each bit to 1 if only one of two bits is 1
~c # 	Inverts all the bits
b << c # Shift left by pushing zeros in from the right and let the leftmost bits fall off
b >> c # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# OPERATOR PRECEDENCE / precedência
# describes the order in wich operations are performed

# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))


# Multiplication '*' has higher precedence than addition '+', and therefore multiplications are evaluated before additions:

print(100 + 5 * 3)

# NOTE: Check the 'operators_precedence-img.png' to understand the order, starting the highest precedence at the top