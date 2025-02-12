
# class is a blueprint (template) 
# empty forma -->

# Name:
# Age:
# Department:
# Employee No.:


# object is a real world entity which holds the information about something

# filled forma -->

# Object1
# Name: Atul
# Age: 24
# Department: QA
# Employee No.: 1234

#Object2
# Name: Roma
# Age: 30
# Department: HR
# Employee No.: 5678

#---------------------------------------------------------


# ------ Defining class ----------------

# form template
class Employee:
    
    def __init__(self, fname, lname, email):
        
        self.fname = fname
        self.lname = lname
        self.email = email
    
    def greet_person(self):

        print("hello, welcome to python class " +self.fname)



# 2 filled form (2 instance of the class)
emp1 = Employee("Atul", "Raman", "atul@gmail.com")
emp2 = Employee("Roma", "Raman", "roma@gmail.com")

print(emp1.fname)  # Atul
print(emp2.email)  # roma@gmail.com


emp1.greet_person()  # hello, welcome to python class Atul
emp2.greet_person()  # hello, welcome to python class Roma



