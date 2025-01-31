# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators


# ------------- A R I T H M E T I C     O P E R A T O R S ----------------

x = 10
y = 5

print(x + y)  # 15
print(x - y)  # 5
print(x * y)  # 50
print(x % y)  # 0
print(x / y)  # 2.0
print(x // y)  # 2
print(x ** y)  # 100000


# ------------- A S S I G N M E N T     O P E R A T O R S ----------------

x = 17

x += 2  # x = x + 2
x -= 2  # x = x - 2
x *= 2  # x = x * 2
x /= 2
x **= 3

print(x)


# ------------- C O M P A R I S O N     O P E R A T O R S ----------------


x = 16
y = 6

# returns Boolean value (T/F)

print(x == y)  # False
print(x != y)  # True
print(x > y)  # True
print(x < y)  # False
print(x <= y)  # False
print(x >= y)  # True


# ------------- L O G I C A L     O P E R A T O R S ----------------


x = 10
y = 0

# returns T/F

print(x == y and x > y)  # False
print(x == y or x > y)  # True


# ------------- I D E N T I T Y      O P E R A T O R S ----------------


# objects are compared

x = ["Atul", "Raman"]
y = ["Atul", "Raman"]

print(x == y)  # comapres the content --> True
# comapres the objet --> False  ( two seprate objects of x and y gets created)
print(x is y)
print(x is not y)  # true


# ------------- M E M B E R S H I P      O P E R A T O R S ----------------


x = ["Atul", "Raman"]

# verifies whether value is in the list or not

print("Atul" in x)     # True
print("Roma" not in x)    # True


# ------------- B I T W I S E      O P E R A T O R S ----------------


# &  -> and
# |  -> or
# ~  -> not
# ^  -> XOR


# 0  -> 00
# 1  -> 01
# 2  -> 10
# 3  -> 11

x = 1
y = 0
print(x & y)  # 0

x = 1
y = 3
print(x | y) # 3


