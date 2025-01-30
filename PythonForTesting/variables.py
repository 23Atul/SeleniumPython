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
