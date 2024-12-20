var_name = input("Variable Name: ")
new_var = ""

for c in var_name:
    if c.isupper():
        print("_" + c.lower(), end="")
#        new_var += "_" + c.lower()
    else: 
        print(c, end="")
#        new_var += c
# if new_var[0] == "_":
#   new_var = new_var[1:]

# optimized code by professor below     
