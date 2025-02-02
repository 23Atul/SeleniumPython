
# ----------------------- S E T S ----------------------------------

# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.

# defining a set

set1 = {10, 20, 30, 40, 50}
set2 = {"Atul","Roma","Ram","Amit","Krishna"}
set3 = {10,"Atul",99.99,True,None}  # set can hold any data type or combination of different data types.


#sets do not maintain the order as it is unordered collection of elements.
print(set1)  # {50, 20, 40, 10, 30}
print(set2)  # {'Roma', 'Atul', 'Krishna', 'Amit', 'Ram'}
print(set3)  # {None, True, 99.99, 'Atul', 10}


# sets do not accept the duplicate values
set4 = {10,20,30,10,40,50,10,60,70,10,80,90,10}

print(set4)  # {70, 40, 10, 80, 50, 20, 90, 60, 30} # eleminates the duplicate value


# defining using set method  :- set((items))

set5 = set((1,2,3,4,5,6))
print(set5)  # {1, 2, 3, 4, 5, 6}

set6 = set((1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,))
print(set6)  # {1, 2, 3, 4}
 


# creating empty set

set7 = {}
print(set7, type(set7))  # {} <class 'dict'>

# we cannot define an empty set using {} as it will create an empty dictionary and not empty set, 
# to create empty set we must use set method set()

set8 = set()
print(set8, type(set8))  # set() <class 'set'>



# length of set :- len()

set9 = {10,20,30,40,50,50}
print(len(set9))  # 5




# membership operator in set

set10 = {10,20,30,40,50,60,70,80,90,100}

print(30 in set10) # True
print(99 in set10) # False

