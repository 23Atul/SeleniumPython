
# ------------------- F U N C T I O N S ------------------------

# functions are the reusable piece of code

# traditional approach

x = 10
y = 23
z = x + y
print(z) # 33


a = 99
b = 101
c = a + b
print(c) # 200



# using functions

def addition1():
    print(23+10)

addition1() # 33

#---------------------------------

x=99
y=101
def addition2():
    print(x+y)

addition2()  # 200

# ------------------------------------


def addition3(p,q):  # parameters
    print(p+q)

addition3(23,33) # 56  # arguments
addition3(99,101) # 200  # arguments

