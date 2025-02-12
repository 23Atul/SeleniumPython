
# inheritance ---> properties and functions given by parent to their child

class ParentClass:

    def __init__(self):
        print("Parent class instance")

    
    def parent_method(self):
        print("parents money")



class ChildClass(ParentClass):   # ChildClass inheriting properties of ParentClass

    pass




p = ParentClass()  # Parent class instance
p.parent_method()  # parents money


c = ChildClass()   # Parent class instance
c.parent_method()  # parents money
# inheriting from parent class




# --------------------------------------------------------------------------------------




class RateOfInterest:

    interest = 0.09

    def __init__(self, name, loan):
        self.name = name
        self.loan = loan

    def calcInterest(self):
        print("interest is: ", self.loan * self.interest)



class student(RateOfInterest):  # inheriting properties and functions of parent class RateOfInterest

    interest = 0.04  # lower rate of interest for students 



r2 = RateOfInterest("Amit", 500000)
r2.calcInterest()  # interest is:  45000.0

r1 = student("Atul", 500000)
r1.calcInterest()  # interest is:  20000.0