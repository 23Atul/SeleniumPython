
# normal read and write methods

fw = open("writeDemo.txt", "w", encoding="utf-8")
fw.write("Hello World")
fw.close()

fr = open("writeDemo.txt", "r", encoding="utf-8")
print(fr.read())  # Hello World
fr.close()


#-------------------------------------------------------------------------



# read and write methods without  closing the file

# we have to close every opened file

fw = open("writeDemo.txt", "w", encoding="utf-8")
fw.write("Hello Atul")
# fw.close()

fr = open("writeDemo.txt", "r", encoding="utf-8")
print(fr.read())  # nothing gets printed
# fr.close()


# -------------------------------------------------------------------------


# ------------------ W I T H   K E Y W O R D ------------------------------

with open("writeDemo.txt","w",encoding="utf-8") as fw:
    fw.write("demo line to test with keyword")

with open("writeDemo.txt","r", encoding="utf-8") as fr:
    print(fr.read())  # demo line to test with keyword

# here we are not bound to close the file everytime, with keyword will take care of it.


# It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try -finally blocks:
