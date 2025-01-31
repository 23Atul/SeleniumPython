
# ------------------- S T R I N G    M E T H O D S -------------------------


#   len(s)      -->     Returns length of string or the numbers of items in an object

name = "Atul Raman"
print(len(name)) # 10



#   str()       -->     Converts specifiedvalue into a String.  --> do not change the original value to change it we nec=d to assign them in variable

phone = 6206020674
print(type(phone))  # <class 'int'>
phone=str(phone)
print(type(phone))  # <class 'str'>




#   upper()     -->     converts a string into upper case and returns a copy 

name = "atul raman"
print(name.upper()) # ATUL RAMAN
print(name) # atul raman  --> do not modifies the original string




#   count(sub, start,end)     -->     Returns the number of time a specified value is found in the string

bio = "driven front end engineer with expertise in JS HTML CSS and React"

print(bio.count("e")) # 9 --> particular character
print(bio.count("en")) # 3 --> sub-string
print(bio.count("e", 2, 30))  # 5 --> "e" appeared 5 times in between index 2 and 30





#   isupper(), islower()    -->     Returns True if all characters in string are upper case or lower case respectively

name="atul raman"
print(name.islower()) # True

NAME = name.upper() # converting name to upper case
print(NAME) # ATUL RAMAN
print(NAME.isupper()) # True





#   split (seperator)        -->     splits the string at specified seperator and returns a list([])  

str1 = "My name is Atul Raman and I am an engineer."

arr = str1.split()    

print(arr)      # ['My', 'name', 'is', 'Atul', 'Raman', 'and', 'I', 'am', 'an', 'engineer.']

print(str1)  # My name is Atul Raman and I am an engineer.   --> do not modify original string


# rsplit(seperator)     -->      splits string into list starting from right

str2 = "My name is Atul Raman and I am an engineer."

arr = str2.rsplit(" ")
print(arr)




#   strip(character)     -->     Returns the trimmed version of the string, trims the string for specfied character ..by default is whitespace

str3 = "           My Name Is Atul Raman And I Am An Engineer                "

x = str3.strip()
print(x)  #  "My Name Is Atul Raman And I Am An Engineer"
print(str3)  #  "           My Name Is Atul Raman And I Am An Engineer                "  # do not modify the original string

#lstrip()
print(str3.lstrip())  # "My Name Is Atul Raman And I Am An Engineer                "

#rstrip()
print(str3.rstrip())  # "           My Name Is Atul Raman And I Am An Engineer"





#   replace(old, new, count (optional))     -->     replaces the specified phrase with another specified phrase

str4 = "My name is Atul Raman and I am an engineer."

x = str4.replace("m","@")

print(x)   # My na@e is Atul Ra@an and I a@ an engineer.
print(str4)  # My name is Atul Raman and I am an engineer.   # do not modify original string


x = str4.replace("a", "#",3 )
print(x)  # My n#me is Atul R#m#n and I am an engineer.  #replaces only 3 a with # rest all a are as it is






#   find( sub, start, end)      -->     searches specified value in the string and returns the postion of the first match else returns -1

str5 = "My name is Atul Raman and I am an engineer."

print(str5.find("Atul"))  # 11

print(str5.find("ATUL"))  # -1

print(str5.find("My", 5 ,10)) # -1






#    index(sub, start, end)     -->     same as find but raises value error when specified value is not found

str6 = "My name is Atul Raman and I am an engineer."

print(str6.index("Atul")) # 11
print(str6.index("atul"))  # ValueError: substring not found
