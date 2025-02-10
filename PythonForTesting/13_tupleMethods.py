
# count(el) ---> count the number of times the element was repeated

tup = (1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9)

print(tup.count(2))  # 7


# index(el)  ---> returns the index of matching character

tup = ("Atul", "Raman", "Ram", "Kumar", "Raman")

print(tup.index("Kumar"))  # 3
# print(tup.index("Amit"))  # ValueError: tuple.index("Amit"): Amit not in tuple


# accesing using loop

for x in tup:
    print(x)

# Atul
# Raman
# Ram
# Kumar
# Raman



# join--> "+"  --> joins two or more tuples and returns a new tuple

tup1 = (1, 2, 3)
tup2 = ("a", "b", "c")
tup3 = (True, False)
tup = tup1 + tup2 + tup3 

print(tup)  # (1, 2, 3, 'a', 'b', 'c', True, False)
# tup4 = (99.999)


# tup = tup1 + tup2 + tup3 + tup4
print(tup)  # TypeError: can only concatenate tuple (not "float") to tuple



# index oprations 


tupMix = (1, 999, 2, 3, "a", "b", "c", True, 999, False, 23.56, "Atul")

print(tupMix[:])  # (1, 999, 2, 3, 'a', 'b', 'c', True, 999, False, 23.56, 'Atul')
print(tupMix[1:5])  # (999, 2, 3, 'a')

print(tupMix[-1]) # Atul

