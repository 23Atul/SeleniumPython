# operators of same precedence will follow Left --> Right order

print(5 + 8 - 2)  # 11 --->> 5 + 8 = 13 - 2 = 11
print(5 - 8 + 2)  # -1 --->> 5 - 8 = -3 + 2 = -1


print(5 - (8 + 2)) # -5 --->> 5 - (10) = -5  () has more precedence


#---------------------------------------------------------------------------------------------

# Highest to Least,   Left to Right  -->

# 1.    [expression], {key:value} { expression}

# 2.    (expression)

# 3.    **

# 4.    *, /, //, %

# 5.    +, -

# 6.    not

# 7.    and 

# 8.    or

# 9.    if-else

# 10.   =