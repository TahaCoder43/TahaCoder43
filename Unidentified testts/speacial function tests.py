# It is used to determine the type of data
list1 = ["Taha", "Shan", "Aliya"]
variable = 21
tuple = ("this", "is", "a", "tuple")
dictionary = {

    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    0

}

print(type(list))
print(type(dictionary))
print(type(tupl))

# This is the list function it converts a tuple or anything into a list
tuple = ('Taha', 14, 'Rawalpindi')
try :
    tuple[1] = '15'
except TypeError :
    print("Tuple can't be changed")

list2 = list(tuple)
list2[1] = 15
print(list2)

test_subject = "lol"
test_subject_2 = "lolo"