
# modules: piece of code which can be used anywhere in any file or folder ny simply just importing that module.

# we want to use the functions defined in myfirstModule.py file but we dont want to rewrite the whole code here as well, so we can simply import the module here.

from math import factorial

from myModule import myfirstModule

myfirstModule.fun1()  # Function1
myfirstModule.fun2()  # function2




# -------------- built-in module --------------------


print(factorial(20))  # 2432902008176640000
print(factorial(4))   # 24


