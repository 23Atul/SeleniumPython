
class AreaRect:
    
    def __init__(self, length, bredth):
        self.length = length
        self.bredth = bredth

    
    def calc_area(self):
        return self.length * self.bredth
    

# x = calc_area()  # NameError: name 'calc_area' is not defined
# the function defined inside the class can't be accessed directly but it can be accessed using the object we created.


area1 = AreaRect(20, 13)
area2 = AreaRect(100,40)

A1 = area1.calc_area()
A2 = area2.calc_area()

print(A1)  # 260
print(A2)  # 4000

        