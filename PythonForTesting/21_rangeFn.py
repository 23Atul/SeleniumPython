
# ---------------- R A N G E    F U N C T I O N --------------------------

# Range is a built in function, It generates the sequence of numbers

# range(start,stop, step)

# the advantage of range over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter thre size of the range it represents.


#---------------------------------------------

arr = [1,2,3,4,5,6,7,8,9,10]
for i in arr:
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# this take a lot of memory as we are defining the list beforehand

#----------------------------------------------------------------------

range(10)  # 0 to 9

for i in range(10):
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#----------------------------------------------------

for i in range(1,11):
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# ----------------------------------------------------------------------

for i in range(2,21,2):
    print(i)

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
