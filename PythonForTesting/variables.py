# variables

username = "Atul"
print(username) #Atul

# Data type of the variable
print(type(username))  # <class 'str'>


# values can be re-assigned
x = 100
print(x) #100

x = 600
print(x) #600

# to know the address or the memory location of variable use id().
a = 800
b = a

print("a: ", a, ", address of a: ", id(a))  # a: 800 , address of a: ...3408
print("b: ", b, ", address of b: ", id(b))  # b: 800 , address of b: ...3408

b += 1

print("a: ", a, ", address of a: ", id(a))  # a: 800 , address of a: ...3408
print("b: ", b, ", address of b: ", id(b))  # b: 801 , address of b: ...4603



# variable convention

# 1. must start with a letter or underscore(_)
# 2. must not start with a number (0-9)
# 3. can only contain alpha-numeric  and underscore (a-z, A-Z, 0-9 , _ )
# 4. should not contain special characters ( !, @, #, $, %, ^, &, *, <, >, ?, /, \, ;, :, [], {}, ())
# 5. variable name should not be a keywords (keyword.kwlist)

import keyword

keywords = keyword.kwlist
print(keywords)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
