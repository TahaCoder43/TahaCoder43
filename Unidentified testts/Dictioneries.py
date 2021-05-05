#dictionery is a key value storage, in which you have to enter the key in order to obtain the value
from typing import Dict, Any, Union

list = ['this','is','sparta']

profile_1 = {"Name": "Taha", "Age": 14, "City": "Rawalpindi"}

Profile_2 = dict(Name="Ali", Age=16, city="Islamabad" )

print(Profile_2)

Profile_2["Country"] = "Pakistan"

print(Profile_2)
print(Profile_2)

print(Profile_2['Name'])
print(profile_1["City"])

#You can use del to delete items from a dictionery

if "Name" in Profile_2:
    print("valid input")
else:
    print("invalid input")
def loop(List):
    for x in list:
        print(x)
loop(list)

for x,y in profile_1.items():
    print(x,y)

profile_1.update(Profile_2)
print(profile_1)


