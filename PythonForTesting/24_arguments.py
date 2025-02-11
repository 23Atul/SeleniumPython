
# ---------------- A R G U M E N T S     I N     P Y T H O N ---------------------------

def subtraction(a,b):   # parameters
    return a-b

x = subtraction(20,15)  # arguments
print(x)



# POSITIONAL ARGUMENTS ----------------------------------------------------

def sub(a, b):   # parameters
    return a-b


x = sub(20, 15)  # arguments
print(x)  # 5

# here a will get 20 and b will get 15 ...so value will depend on its position of arguments. so it is called positionall argument.




# REQUIRED ARGUMENTS ----------------------------------------------------

def mul(a, b):   # parameters
    return a-b


# x = mul()  # arguments
print(x)  # TypeError: mul() missing 2 required positional arguments: 'a' and 'b'

# here a and b are required argument as we must pass the respective value of a nd b as argument.




# OPTIONAL ARGUMENTS ------------------------------------------------

def div(a=5, b=10):   # parameters
    return a*b


print(div())  # 50 a=5 b=10
print(div(6,4)) # 24  a=6 b=4
print(div(8)) # 80  a=8 b=10

# we can define the default value to the paramenters so that it can be used in case we do not pass any value as an argument 





# KEYWORD ARGUMENTS -------------------------------------------------------


def add(a=10, b=9):   # parameters
    return a+b


print(add())  # arguments

print(add(30)) # 39  a=30 b=9
print(add(b=30)) # 40  a=10  b=30


#  if there are many default paramenters and we pass the value as argument, due to poisitional argument it will be assigned to 1st parameter.
#  but if we want to specify that value to some other parameter then we use keyword argument.



