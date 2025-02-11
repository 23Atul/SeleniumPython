
# zip() ---> takes two or more iterables (list, tuple, set, dictionary) and maps their values to the respective indexed values and returns the list of tupples.

country = ["India", "Pakistan", "Bangladesh", "Nepal", "USA"]
city = ["Delhi", "Islamabad", "Dhaka", "Kathmandu", "California"]

s = zip(country,city)

print(s)  # <zip object at 0x1007dd800>

print(list(s)) 
#[('India', 'Delhi'), ('Pakistan', 'Islamabad'), ('Bangladesh', 'Dhaka'), ('Nepal', 'Kathmandu'), ('USA', 'California')]



# mismatch count  --> maps one to one ...leaving the extra one

ountry = ["India", "Pakistan", "Bangladesh", "Nepal", "USA"]
city = ["Delhi", "Islamabad", "Dhaka", "Kathmandu", "California", "Mumbai"]

s = zip(country, city)
print(list(s))
# [('India', 'Delhi'), ('Pakistan', 'Islamabad'), ('Bangladesh', 'Dhaka'), ('Nepal', 'Kathmandu'), ('USA', 'California')]




# --------------------- USE CASE -----------------------

country = ["India", "Pakistan", "Bangladesh", "Nepal", "USA"]
city = ["Delhi", "Islamabad", "Dhaka", "Kathmandu", "California"]

for x, y in zip(country,city):
    print(x,y)

# India Delhi
# Pakistan Islamabad
# Bangladesh Dhaka
# Nepal Kathmandu
# USA California




costPrice = [300,500,90,899,5000]
sellingPrice = [400,450, 80,920,8000]
profits = []

for x, y in zip(costPrice,sellingPrice):
    print("profit",y-x)
    profits.append(y-x)

print(profits)

# profit 100
# profit - 50
# profit - 10
# profit 21
# profit 3000
# [100, -50, -10, 21, 3000]
