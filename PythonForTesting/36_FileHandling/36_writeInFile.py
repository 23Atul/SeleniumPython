
# ---------------- file handling ----------------------

# file input and file output


# Manual steps to write in a file

# 1. Open notepad and create file
# 2. Write in the file
# 3. Close the file



# in python there are methods and function available which does the same task of opening, reading, writing, closing a file, but not manually


# open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: 
# open(filename, mode, encoding=None)    eg. f = open('workfile', 'w', encoding="utf-8")


# Mode
# Read mode: r
# Write mode: w
# Append mode: a
# Read/write: r+


f = open("writeDemo.txt", "w", encoding="utf-8")  # open a file
f.write("this is first line")  # write in a file
f.close()  # close a file
# a file name writeDemo.txt gets created in the same folder with the content written in it

# --------------------------------------------------------------------------------------------



# creating file at a specific location

f = open("/Users/atul/Desktop/PythonSelenium Testing/writedemo1.txt","w", encoding="utf-8")
f.write("this is first line")  # write in a file
f.close()  # close a file
# new txt file gets created in the file location



# ------------------------------------------------------------------------------------


# writing actual data in a file

f = open("writeDemo.txt", "w", encoding="utf-8")
arr = [2,3,4,5,5,6,7,7,6,88,0]
for item in arr:
    f.write(str(item)+"\n")     # accepts only string

f.close()

# write method will overwite the file...but we dont want to overwrite it so we use append method.

f = open("writeDemo.txt", "a", encoding="utf-8")
arr = [2, 3, 4, 5, 5, 6, 7, 7, 6, 88, 0]
for item in arr:
    f.write(str(item)+"\n")     # accepts only string

f.close()
