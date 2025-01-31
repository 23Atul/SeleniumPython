
# -------------------------- S T R I N G      F O R M A T I N G ------------------------------------


# not so correct approach
print("Welcome to online class of Automation Testing using Selenium Python.")

x = "Automation Testing"
y = "Selenium Python"


# good but not so affective
print( "Welcome to online class of "+x+" using "+y+".")  # Welcome to online class of Automation Testing using Selenium Python.

# can be improved more
print("welcome to online class of %s using %s." % (x, y))    # welcome to online class of Automation Testing using Selenium Python.

# can be used when no. of variables are less
print("welcome to online class of {0} using {1}.".format(x, y))  # welcome to online class of Automation Testing using Selenium Python.

# or
print("welcome to online class of {course} using {teckstack}.".format(course=x, teckstack=y))  # welcome to online class of Automation Testing using Selenium Python.


