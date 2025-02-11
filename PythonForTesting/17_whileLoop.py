#   used to iterate block of code as long as test expresssion is true.
#   test expresssion is checked first, if expression is evaluated to true then body of loop is executed.
#   conditions are used to stop the loops
#   can iterate on list, string, tuples,dictionary


# syntax

# while test_expression:
#     body of while loop


x = 0
print("going inside while loop")
print()

while x <= 10:
    print("inside while loop", x)
    x += 1

print()
print("out of while loop")


# going inside while loop

# inside while loop 0
# inside while loop 1
# inside while loop 2
# inside while loop 3
# inside while loop 4
# inside while loop 5
# inside while loop 6
# inside while loop 7
# inside while loop 8
# inside while loop 9
# inside while loop 10

# out of while loop



# loop on strings ----------------------

city = "Hyderabad"
x = 0

while x < len(city):
    print(city[x])
    x = x+1

# H
# y
# d
# e
# r
# a
# b
# a
# d




# loop on lists ------------------------------------------

arr = ["Atul","Raman","Ram","Krishna","Amit","Roma"]
i=0

while i < len(arr):
    print(arr[i])
    i+=1

# Atul
# Raman
# Ram
# Krishna
# Amit
# Roma
