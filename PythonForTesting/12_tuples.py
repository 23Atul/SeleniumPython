
# Tuples ---> Tuples are indexed, allow duplicate values and cannot be modified (immutable).


# defining a tuple -----------------------------

tup = (1, 2, 3, 4)
print(tup)  # (1, 2, 3, 4)
print(type(tup))  # <class 'tuple'>


tupStr = ("a", "b", "c")
tupBool = (True, False, True)


tupMix = (1, 2, 3, "a", "b", "c", True, False, 23.56, "Atul")


# accessing tuples -------------------

tupMix = (1, 999, 2, 3, "a", "b", "c", True, 999, False, 23.56, "Atul")

print(tupMix[0]) # 1



# modifying tuples---> tuples can't be modified ----------------------

tupMix = (1, 999, 2, 3, "a", "b", "c", True, 999, False, 23.56, "Atul")

# tupMix.append("Raman")

print(tupMix)  # AttributeError: 'tuple' object has no attribute 'append'


# tupMix[1] = 10
print(tupMix)  # AttributeError: 'tuple' object has no attribute 'append'


print(len(tupMix)) # 12
