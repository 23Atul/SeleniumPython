
# ---------------------- L I S T S      M E T H O D S -----------------------------


# list.append(item) :- appends an item at the end of the list.

arr = [10,20,30,40,50]

arr.append(999)
print(arr)  # [10, 20, 30, 40, 50, 999]



# list.insert(index,item) :- inserts the item at a given position or index.

arr = [10,20,30,40,50]

arr.insert(3,888)
print(arr)  # [10, 20, 30, 888, 40, 50]




# list.remove(item) :- removes the first item from the list whose value is equal to item

arr = [10, 20, 30, 10, 50]

arr.remove(10)
print(arr)  # [20, 30, 10, 50]




# list.pop([i]) :-  revmoves and returns the item at specified position or index, if no index is specified then removes the last item in the list.

arr = [10,20, 30, 40, 50]

x=arr.pop(1)
print(x)  # 10
print(arr)  # [10, 30, 40, 50]

x = arr.pop()
print(x)  # 50
print(arr)  # [10, 30, 40]



# list.index(x,start,end) :- returns the index of first matching value.

arr = [10,20,30,40,50]

print(arr.index(20)) # 1
# print(arr.index(99))  # ValueError: 99 is not in list



# list.count(item) :- returns the number of times, item appears in the list.

arr = [10,20,30,10,40,50,10,60,70,10,80,90,10,100]

print(arr.count(10))  # 5




# list.sort() :- sort the items of list in place, modifies original array

arr = [30,10,50,40,5]
print(arr.sort()) # None
print(arr)  # [5, 10, 30, 40, 50]



# list.reverse() :- Reverse the elements of the list in place

arr = [10, 20, 30, 40, 50]
print(arr.reverse())  # None
print(arr)  # [50, 40, 30, 20, 10]




# list.copy() :- creates the shallow copy of the list. equivalent to arr[:]

arr = [10,20,30,40,50]
arr1=arr.copy()
print(arr)  # [10, 20, 30, 40, 50]
print(arr1)  # [10, 20, 30, 40, 50]

arr1[0]=999

print(arr)  # [10, 20, 30, 40, 50]
print(arr1)  # [999, 20, 30, 40, 50]




# list.remove(item) :-  removes the first match of the specified item from the list.

arr = [10,20,30,40,999,50,60,999]

print(arr.remove(999)) # None
print(arr) # [10, 20, 30, 40, 50, 60, 999]




# list.clear() :- clears the whole list

arr = [10,20,30,40]

print(arr.clear()) # None
print(arr) # []


