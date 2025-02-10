
#-----------------------  S E T     M E T H O D S -----------------------------------

# add(elem) --> Add elemets to the set.

set1 = {1,2,3,4,5}
set1.add(6)
print(set1) # {1,2,3,4,5,6}

set2 = set()
set2.add(0)
print(set2) # {0}



# remove(elem) --> removes the element from set if present else raises a keyError

set3 = {1,2,3,4,999,5,6,7,8}

print(set3.remove(999)) # None
print(set3)  # {1, 2, 3, 4, 5, 6, 7, 8}

# print(set3.remove(888))  # KeyError: 888
# print(set3)




# discard(elem) --> removes the element if present

set4 = {1,2,3,4,999,5,6,7,8}
print(set4.discard(999)) # None
print(set4)  # {1, 2, 3, 4, 5, 6, 7, 8}

# print(set4.remove(888))  # KeyError: 888
# print(set4)




# pop()  ---> removes and returns an arbitrary  value from set, raises key error if set is empty.

set5 = {1,2,3,4,5,999,6,7,8}
print(set5.pop()) # 1
print(set5)  # {2, 3, 4, 5, 6, 999, 7, 8}

# set6 = set()
# print(set6.pop())  # KeyError: 'pop from an empty set'




# clear()  --->  removes all element from set

set7 = {1,2,3,4,5,6,7,8,9}
print(set7.clear()) # None
print(set7) # set()




# ----------- Joining two sets -----------------------


# union()  --> joines two set to make one set containing all value, returns different set

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

x = setA.union(setB)
print(x)  # {1, 2, 3, 4, 5, 999, 'a', 'b', 'c'} # removes the duplicate value, returns the new set



# update()  -->  update the set by doing union operation on set itself. 

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

setA.update(setB)
print(setA)  # {1, 2, 3, 4, 5, 'a', 999, 'c', 'b'}
print(setB)  # {'c', 'b', 'a', 999}





# ----------- Keeping only duplicate -----------------------


# intersection()  --> returns the intersection of two sets ie. returns only the common elements in the set as a new set.

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

x = setA.intersection(setB)
print(x)  # {999}


# intersection_update()  -->  updates the set with only the intersection values

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

setA.intersection_update(setB)
print(setA)  # {999}
print(setB)  # {'a', 'c', 'b', 999}





# ----------- Keep all excluding duplicate -----------------------

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}


# symmetric_difference()

x = setA.symmetric_difference(setB)
print(x)  # {1, 2, 3, 4, 5, 'c', 'b', 'a'}


# symmetric_difference_update()

setA.symmetric_difference_update(setB)
print(setA)  # {'b', 1, 2, 3, 4, 5, 'c', 'a'}
print(setB)  # {'b', 'c', 'a', 999}


# -----------------------  S E T     M E T H O D S -----------------------------------

# add(elem) --> Add elemets to the set.

set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(set1)  # {1,2,3,4,5,6}

set2 = set()
set2.add(0)
print(set2)  # {0}


# remove(elem) --> removes the element from set if present else raises a keyError

set3 = {1, 2, 3, 4, 999, 5, 6, 7, 8}

print(set3.remove(999))  # None
print(set3)  # {1, 2, 3, 4, 5, 6, 7, 8}

# print(set3.remove(888))  # KeyError: 888
# print(set3)


# discard(elem) --> removes the element if present

set4 = {1, 2, 3, 4, 999, 5, 6, 7, 8}
print(set4.discard(999))  # None
print(set4)  # {1, 2, 3, 4, 5, 6, 7, 8}

# print(set4.remove(888))  # KeyError: 888
# print(set4)


# pop()  ---> removes and returns an arbitrary  value from set, raises key error if set is empty.

set5 = {1, 2, 3, 4, 5, 999, 6, 7, 8}
print(set5.pop())  # 1
print(set5)  # {2, 3, 4, 5, 6, 999, 7, 8}

# set6 = set()
# print(set6.pop())  # KeyError: 'pop from an empty set'


# clear()  --->  removes all element from set

set7 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set7.clear())  # None
print(set7)  # set()


# ----------- Joining two sets -----------------------


# union()  --> joines two set to make one set containing all value, returns different set

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

x = setA.union(setB)
# {1, 2, 3, 4, 5, 999, 'a', 'b', 'c'} # removes the duplicate value, returns the new set
print(x)


# update()  -->  update the set by doing union operation on set itself.

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

setA.update(setB)
print(setA)  # {1, 2, 3, 4, 5, 'a', 999, 'c', 'b'}
print(setB)  # {'c', 'b', 'a', 999}


# ----------- Keeping only duplicate -----------------------


# intersection()  --> returns the intersection of two sets ie. returns only the common elements in the set as a new set.

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

x = setA.intersection(setB)
print(x)  # {999}


# intersection_update()  -->  updates the set with only the intersection values

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}

setA.intersection_update(setB)
print(setA)  # {999}
print(setB)  # {'a', 'c', 'b', 999}


# ----------- Keep all excluding duplicate -----------------------

setA = {1, 2, 3, 4, 5, 999}
setB = {"a", "b", "c", 999}


# symmetric_difference()

x = setA.symmetric_difference(setB)
print(x)  # {1, 2, 3, 4, 5, 'c', 'b', 'a'}


# symmetric_difference_update()

setA.symmetric_difference_update(setB)
print(setA)  # {'b', 1, 2, 3, 4, 5, 'c', 'a'}
print(setB)  # {'b', 'c', 'a', 999}





# ----------- Returns set containing difference between two or more sets -----------------------

# difference()  --> returns the new set with difference of one set w.r.t other

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9}

x = setA.difference(setB)
print(x)  # set()  # all value in setA are there in setB

x = setB.difference(setA)
print(x)  # {8, 9, 6, 7} # difference of setB w.r.t setA


# difference_update()

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9}

setA.difference_update(setB)
print(setA)  # set()
print(setB)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}



setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9}

setB.difference_update(setA)
print(setA)  # {1, 2, 3, 4, 5}
print(setB)  # {6, 7, 8, 9}


# -----------------------------------------------------------------------------------------------------------



# issubset() --> returns the boolean T or F


setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9}

x = setA.issubset(setB)
print(x)  # True




# issuperset()

x = setA.issuperset(setB)
print(x)  # False

x = setB.issuperset(setA)
print(x)  # True


