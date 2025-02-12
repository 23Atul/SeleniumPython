
# ---------------------- B U I L T - I N     F U N C T I O N S -----------------------------

# max() ---> Returns the largest item in an iterable

arr = [88,20,8237,20120,233,28]
print(max(arr))  # 20120


# min() ---> Returns the smallest item in an iterable

arr = [88, 20, 8237, 20120, 233, 28]
print(min(arr))  # 20



# iter() ---> Returns the iterator object

arr = [88, 20, 8237, 20120, 233, 28]
i = iter(arr)
print(sum(i)) #28726



# reversed() ---> Returns a reversed iterator.

arr = [88, 20, 8237, 20120, 233, 28]
rev = reversed(arr)
print(next(rev))
print(arr)



# next() ---> 


# slice(start, end, step) --->  Returns a slice object

arr = [88, 20, 8237, 20120, 233, 28]
x = arr[slice(2, 5)]  # [8237, 20120, 233]
print(x)



# sorted() --> Returns the sorted list

arr = [88, 20, 8237, 20120, 233, 28]
x = sorted(arr)
print(x)  # [20, 28, 88, 233, 8237, 20120]
print(arr)  # [88, 20, 8237, 20120, 233, 28]




# sum() ---> sums the items of an iterator

arr = [88, 20, 8237, 20120, 233, 28]
x = sum(arr)
print(x)  # 28726

y = sum(arr,5)
print(y)  # 28731   # adds 5 to the array sum




# input()  --->  allows the user to input value

name = input("enter your name")
print("welcome "+ name)






# A
# abs()
# aiter()
# all()
# anext()
# any()
# ascii()

# B
# bin()
# bool()
# breakpoint()
# bytearray()
# bytes()

# C
# callable()
# chr()
# classmethod()
# compile()
# complex()

# D
# delattr()
# dict()
# dir()
# divmod()

# E
# enumerate()
# eval()
# exec()

# F
# filter()
# float()
# format()
# frozenset()

# G
# getattr()
# globals()

# H
# hasattr()
# hash()
# help()
# hex()

# I
# id()
# input()
# int()
# isinstance()
# issubclass()
# iter()
# L
# len()
# list()
# locals()

# M
# map()
# max()
# memoryview()
# min()

# N
# next()

# O
# object()
# oct()
# open()
# ord()

# P
# pow()
# print()
# property()


# R
# range()
# repr()
# reversed()
# round()

# S
# set()
# setattr()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()

# T
# tuple()
# type()

# V
# vars()

# Z
# zip()

# _
# __import__()
