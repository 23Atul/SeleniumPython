
# Dictionaries ---> Dictionaries are used to store data in key:value pairs. They are changable and do not allow duplicate values.


# Defining Dictionaries -------------------

dict1 = {}

print(dict1, type(dict1))  # {} <class 'dict'>


user = {
    "name": "Atul",
    "age" : 24
}

print(user)  # {'name': 'Atul', 'age': 24}



# Accessing items from Dictionaries -----------------------

user = {
    "name": "Atul",
    "age": 24
}

print(user["name"])  # Atul



# Adding items to Dictionaries --------------------------

user = {
    "name": "Atul",
    "age": 24
}

user["city"]="Ranchi"

print(user)  # {'name': 'Atul', 'age': 24, 'city': 'Ranchi'}




# Removing items from Dictionaries --------------------------------

user = {
    'name': 'Atul', 
    'age': 24, 
    'city': 'Ranchi'
}

print(user.pop("city"))  # Ranchi --> returns the poped item
print(user)  # {'name': 'Atul', 'age': 24}


