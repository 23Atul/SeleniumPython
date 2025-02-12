
# exceptions -->   https://docs.python.org/3/library/exceptions.html#bltin-exceptions


print("Input first number")
x = int(input())

print("Input second number")
y = int(input())


print(x/y)  # x = 10, y = 0   o/p: ZeroDivisionError: division by zero


# -------------------------------------------------------------------------------


try :

    print("Input first number")
    x = int(input())

    print("Input second number")
    y = int(input())


    print(x/y)

except ZeroDivisionError as e:
    print("exception error: ",e)



# x = 10
# y = 0
# o/p: exception error: division by zero


# ---------------------------------------------------------------------------


try:

    print("Input first number")
    x = int(input())

    print("Input second number")
    y = int(input())

    print(x/y)

except Exception as e:
    print("exception error: ", e)

else:
    # executed only when code has no error or does not go in except block
    print("in else block")

finally:
    print("this is always executed")  # gets executed everytime code runs


#----------------------------------------------------------------------------------------



# raise Exception:  raises error when the condition satisfies


try:

    print("Input first number")
    x = int(input())

    print("Input second number")
    
    if y == 0:
        raise Exception("division with 0 is not possible")
    y = int(input())

    print(x/y)

except ValueError as e:
    print("exception error: ", e)

else:
    # executed only when code has no error or does not go in except block
    print("in else block")

finally:
    print("this is always executed")  # gets executed everytime code runs




