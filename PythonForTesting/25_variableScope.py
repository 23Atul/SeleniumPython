
# Variable scope in Python - boundary of variables within a program

# when we define a variable and assign any value to it, we can print its value by accessing it, but we can't access variable from everywhere.





# Local Scope

def var_scope1():
    x = 20
    print(x)

var_scope1()  # 20
# print(x)  # NameError: name 'x' is not defined

# error comes because x has a local scope or the functional scope and its boundry is restricted within its function only, it cant be accessed outside the function.

#------------------------------------------------------------------------------





# Global Scope

x = 40  # x has a global scope
def var_scope2():
    print(x)


var_scope2()  # 40
print(x) # 40

# x has a global scope and can be accessed from anywhere.

#-------------------------------------------------------------------------------





# global keyword

# even though a varible has a local or functional scope  we can make it behave like global variable using global keyword.

def var_scope3():

    # global x2 
    x2 = 99
    print(x2)


var_scope3()  # 99
# print(x2)  # 99

#----------------------------------------------------------------------------------------------------





# LEGB rule: Local -> Enclosing -> Global -> Built-in  
# ( built-in has the highest priority ) --> can be accessed from anywhere in a python code


# Local --->  every function has its own local variable and it will be prefered as its value

x = 0

def variable_scope1():
    x = 10
    print("parent ", x)
    
    def child_scope():
        x = 20
        print("child ",x)

        def grandChild_scope():
            x = 30
            print("grandchild ", x)

            def greatGrandChild_scope():
                x = 40
                print("greatGrandChild ", x)


            greatGrandChild_scope()
        
        grandChild_scope()
    
    child_scope()

            
variable_scope1()
print("global ",x)


# parent  10
# child  20
# grandchild  30
# greatGrandChild  40
# global 0

#--------------------------------------------------------


# Enclosing  --->  if any block of function has not defined the value of x then it will take the enclosing value ie. value of x which its parent holds.

x = 0

def variable_scope2():
    x = 10
    print("parent ", x)

    def child_scope():
        
        print("child ", x)

        def grandChild_scope():
            x = 30
            print("grandchild ", x)

            def greatGrandChild_scope():
                
                print("greatGrandChild ", x)

            greatGrandChild_scope()

        grandChild_scope()

    child_scope()


variable_scope2()
print("global ", x)


# parent  10
# child  10
# grandchild  30
# greatGrandChild  30
# global 0

#----------------------------------------------------------------------------





# Global  --->  if no value is assigned in any of the levels then it will take the value assigned in global scope.


x = 0


def variable_scope3():

    print("parent ", x)

    def child_scope():

        print("child ", x)

        def grandChild_scope():

            print("grandchild ", x)

            def greatGrandChild_scope():

                print("greatGrandChild ", x)

            greatGrandChild_scope()

        grandChild_scope()

    child_scope()


variable_scope3()
print("global ", x)


# parent  0
# child  0
# grandchild  0
# greatGrandChild  0
# global 0
