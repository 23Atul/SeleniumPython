
# read data from writeDemo.txt file and print on console

f = open("writeDemo.txt", "r", encoding="utf-8")
print(f.read())  # reading whole file at ones
f.close()

# "My Name is Atul Raman"
# "I am 24 years old"
# "I am a software engineer"
# "I have done a b.tech from CV Raman Global University"
# "Ok, Thank You, Byee Byee"




f = open("writeDemo.txt", "r", encoding="utf-8")

# reading file line-by-line
print(f.readline())   # "My Name is Atul Raman"
print(f.readline())   # "I am 24 years old"
print(f.readline())   # "I am a software engineer"

f.close()
