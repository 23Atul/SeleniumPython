# --------------------------Class Variable vs Instance Variables -------------------


# Instance Variable ---> any variable declared inside the __init__ function in class is known as instance variable

class RateOfInterest1:
    
    def __init__(self, name, loan, interest):

        # name and loan are the instance variables
        self.name = name
        self.loan = loan
        self.interest = interest


    def calcInterest(self):
        print("total interest: ", self.loan * self.interest)


p1 = RateOfInterest1("Atul", 50000, 0.06)
p1.calcInterest()  # total interest:  3000.0

p2 = RateOfInterest1("Roma", 100000, 0.06)
p2.calcInterest()  # total interest:  6000.0





# class Variable --->  when we know that any variable which is fixed for every instance of class then we can define them as a class variable 
# any variable which is defined inside the class and outside any other methods then it is called class variable.

class RateOfInterest2:

    interest = 0.06  # class variable --> accessable to all the class objects.

    def __init__(self, name, loan):

        # name and loan are the instance variables
        self.name = name
        self.loan = loan

    def calcInterest(self):
        print("total interest: ", self.loan * self.interest)
        print("total interest: ", self.loan * RateOfInterest2.interest) 
        # we can use class variable like this as well




p1 = RateOfInterest2("Atul", 50000)
p1.calcInterest()  # total interest:  3000.0


p2 = RateOfInterest2("Roma", 100000)
p2.interest = 0.09  # we can even change the class variable when we want to.
p2.calcInterest()  # total interest:  9000.0

# we can use class variable like this as well
RateOfInterest2.interest = 0.04
p2.calcInterest()