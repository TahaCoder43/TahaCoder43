from math import *
list=["apple","banana","orange","mango","watermelon"]
print(list[-1])
print(list[2])

fruit_bundle = ""

print("\n\n\n")
for Fruits in list:
    fruit_bundle=fruit_bundle + Fruits + " "

print(fruit_bundle)

if "cheese burger" in list:
    print("yes")
else:
    print("I need my cheese burger")
print(len(list))


print("appending and inserting item into list")

list.append("Dragon_fruit")
list.insert(2,"lemon")

print("task completed")
print("This is the list")
print(list)

list.append("blue berry")
print(list)
pop_can_be_a_variable = list.pop()
print(list)
print(pop_can_be_a_variable)
lets_check_it_out = list.pop(2)
print(lets_check_it_out)
print(list)
The_remove_function_is_used_when_you_type_in_the_name_that_you_know_and_are_uninformed_of_the_index = list.remove("Dragon_fruit")
list2 = sorted(list)
list3 = reversed(list)

print(list)
print(list2)
print("(")
print(list3)
print(")")
list4=[0] * 12
print(list4)
list5 = list4 + list
print(list5)
This_is_called_step = list5[12::2]
you_can_reverse_it = list5[::-1]
print(This_is_called_step)
print(you_can_reverse_it)

This_is_the_method_if_you_want_to_copy_list_or_it_will_change_the_other_list = list.copy()



This_is_the_method_if_you_want_to_copy_list_or_it_will_change_the_other_list.append("lemon")
print(This_is_the_method_if_you_want_to_copy_list_or_it_will_change_the_other_list)

print(list)
print("look both are different")
list7=[]
list6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list6)
for x in list6:
    y = pow(x,2)
    list7.append(y)

print(list7)
