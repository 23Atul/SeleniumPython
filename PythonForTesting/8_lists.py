# lists --> collection of different/ multiple values ( of any datatypes)


# varables
x = 10
y = "Atul"

# lists

# declaring
x = [10, 20, 30, 40, 50, 60, 70]
y = ["Atul", "Ram", "Amit", "Roma"]

z = [10, "Atul", True, 99.76,]


# accessing
print(x[0])  # 10
print(z[3])  # 99.76

a = [10, 20, 30, 40, 20]  # lists can have duplicate values

arr = [10, 20, 30]
print(type(arr))  # <class 'list'>


# list slicing
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(arr[:])  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(arr[0:5])  # [10, 20, 30, 40, 50]
print(arr[0:10:2])  # [10, 30, 50, 70, 90]


# updating

name = ["ATUL", "roma", "ram", "amit", "krishna"]

print(name)  # ['ATUL', 'roma', 'ram', 'amit', 'krishna']

name[0] = "atul"
print(name)  # ['atul', 'roma', 'ram', 'amit', 'krishna']


# duplicating 
a = [10, 20, 30, 40]
b = a
print(a, id(a))  # [10, 20, 30, 40] # 4373493568
print(b, id(b))  # [10, 20, 30, 40] # 4373493568

b[1] = 999

print(a, id(a))  # [10, 999, 30, 40] # 4373493568
print(b, id(b))  # [10, 999, 30, 40] # 4373493568

b=[1,2,3,4]

print(a, id(a))  # [10, 999, 30, 40] # 4368758464
print(b, id(b))  # [1, 2, 3, 4]      # 4368508544



