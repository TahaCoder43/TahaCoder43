variable_creator = dict()

for x in range(5):
    x = input("enter in your variable name:")
    y = input("enter its value:")
    variable_creator[x] = y
    x = ""
    y = ""
print(variable_creator)
n = input("which one do you want to access")
print(variable_creator[n])


