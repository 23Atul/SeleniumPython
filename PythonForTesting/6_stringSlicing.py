
# ---------------------- S T R I N G      S L I C I N G --------------------------------------

#   s[start : end : step]

#   s[i : j]  --> slice of s from i to j
#   s[i : j : k]  --> slice of s from i to j with k steps


s = "welcome to software testing with selenium and python"

# welcome to software testing with selenium and python  -->>  starting from 0th till end
print(s[0:])

print(s[0:4])  # welc
print(s[4: 19])  # ome to software

print(s[0: 10: 2])   # wloet
print(s[0: len(s): 3])  # wceooweei tseua tn

print(s[:])  # welcome to software testing with selenium and python


print(s[-1])  # n (last character)
print(s[-7:-1])  # pytho
print(s[-7:])  # python


name = " Atul Raman "
print(name[ : : -1])  # namaR lutA  ( reverses a string )


#--------------------------------------------------------------------------------------------


user = "name, age, gender, city"

print(user.index(","))   # 4
print(user[0: user.index(",")])  # name
