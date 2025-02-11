
# ----------------------- M E T H O D S    I N     D I C T I O N A R I E S --------------------------------------


user1 = {
    "fname":"Atul",
    "lname":"Raman",
    "age": 24,
    "gender": "Male",
    "city":"Ranchi"
}


# get() --->  returns the value of specified key in the dictionary.
print(user1.get("fname")) # Atul


# keys() --->  returns the copy of dictionarie's keys in form of list.
print(user1.keys())  # dict_keys(['fname', 'lname', 'age', 'gender', 'city'])


# values() --->  returns the copy of values in the dictionaries in form of list.
print(user1.values())  # dict_values(['Atul', 'Raman', 24, 'Male', 'Ranchi'])


# items() --->  returns the copy of dictionarie's key value pair in form of list
print(user1.items()) # dict_items([('fname', 'Atul'), ('lname', 'Raman'), ('age', 24), ('gender', 'Male'), ('city', 'Ranchi')])


# pop() --->  removes the item with the specified value and returns the removed value
print(user1.pop("city")) # Ranchi
print(user1)  # {'fname': 'Atul', 'lname': 'Raman', 'age': 24, 'gender': 'Male'}


# popitem() --->  removes arbitrary key:value pair and returns it
print(user1.popitem())  # ('gender', 'Male')
print(user1)  # {'fname': 'Atul', 'lname': 'Raman', 'age': 24}


# update() --->  adds the specified key:value pair to dictionary.
print(user1.update({"city": "Ranchi"}))  # None
print(user1) # {'fname': 'Atul', 'lname': 'Raman', 'age': 24, 'city': 'Ranchi'}


# copy() --->  returns a copy of the dictionary.
user1Copy = user1.copy()
print(user1Copy) # {'fname': 'Atul', 'lname': 'Raman', 'age': 24, 'city': 'Ranchi'} 

user1Copy["status"] = "Active"

print(user1) # {'fname': 'Atul', 'lname': 'Raman', 'age': 24, 'city': 'Ranchi'}
print(user1Copy)  # {'fname': 'Atul', 'lname': 'Raman', 'age': 24, 'city': 'Ranchi', 'status': 'Active'}



# clear() --->  removes all the elements from the dictionary, returns the empty dictionary.
print(user1Copy.clear()) # None
print(user1Copy) # {}