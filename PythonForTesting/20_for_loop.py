
# ----------------------- F O R    L O O P ---------------------

# used to iterate over the sequence like list, string, dictionary, set or tuple

city = "Delhi"  # STRING 

for i in city:
    print(i)

# D
# e
# l
# h
# i

#---------------------------------

city = ["Delhi", "Ranchi", "Agra", "Patna"]  # LIST

for i in city:
    print(i)

# Delhi
# Ranchi
# Agra
# Patna

#-------------------------------------


city = ("Delhi", "Ranchi", "Agra", "Patna") # TUPLE

for i in city:
    print(i)

# Delhi
# Ranchi
# Agra
# Patna

#-------------------------------------------------


# NESTED LIST
arr = [["India", "Delhi"], ["Pakistan", "Islamabad"], ["USA", "California"], ["Bangladesh", "Dhaka"], ["UK", "London"]]

for i in arr:
    print(i)

# ['India', 'Delhi']
# ['Pakistan', 'Islamabad']
# ['USA', 'California']
# ['Bangladesh', 'Dhaka']
# ['UK', 'London']


for country, city in arr:
    print("capital of "+country+" is "+city+".")

# capital of India is Delhi.
# capital of Pakistan is Islamabad.
# capital of USA is California.
# capital of Bangladesh is Dhaka.
# capital of UK is London.



#-------------------------------------------------------------

city = {"Delhi", "London", "Mumbai", "Ranchi"} # SET

for i in city:
    print(i)

# Mumbai
# London
# Ranchi
# Delhi


#--------------------------------------------------------------


arr = [["India", "Delhi"], ["Pakistan", "Islamabad"], ["USA", "California"], ["Bangladesh", "Dhaka"], ["UK", "London"]]

distCity = dict(arr) # array --> dictionary
print(distCity)
# {'India': 'Delhi', 'Pakistan': 'Islamabad', 'USA': 'California', 'Bangladesh': 'Dhaka', 'UK': 'London'}


for i in distCity:
    print(i)

# India
# Pakistan
# USA
# Bangladesh
# UK


for i in distCity.items():
    print(i)

# ('India', 'Delhi')
# ('Pakistan', 'Islamabad')
# ('USA', 'California')
# ('Bangladesh', 'Dhaka')
# ('UK', 'London')

for city, country in distCity.items():
    print(city+", "+country)

# India, Delhi
# Pakistan, Islamabad
# USA, California
# Bangladesh, Dhaka
# UK, London


