
# break : Breakes out from the nearest enclosing loop
# continue : Go to the start of the nearest enclosing loop 

# nearest enclosing loop --> if there are nested loops then one which is the nearest defined loop it will efffect that one only.


# ----- break ---------

i = 0
print("going inside while loop")

while i < 10:
    print("inside while loop",i)
    i+=1
    break

print("out of the while loop")

# going inside while loop
# inside while loop 0 
# out of the while loop
    



# ----------- continue --------------

i = 0
print("going inside while loop")

while i < 10:

    i += 1
    continue
    print("inside while loop", i)
    
print("out of the while loop")

# going inside while loop
# out of the while loop




# ------------------- while - else --------------------------- (must be used with break statement)


# without while - else   -----> even if while loops runs then also else part will get executed 

x=0
while x<=10:
    print(x)
    x+=1
else:
    print("out of loop")


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
# 10
# out of loop



# with while - else

x = 0
while x <= 10:
    print(x)
    x += 1
    if x == 7:
        break
else:
    print("out of loop")


# 0
# 1
# 2
# 3
# 4
# 5
# 6
