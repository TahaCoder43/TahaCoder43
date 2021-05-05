lol = {1,2,3,4,5}
print(type(lol))
print(lol)
lol.add("me")
print(lol)
lol.remove(3)
print(lol)
lol.discard(12)
print(lol)
print(lol.pop())
# Messing merge and difference annd things like this don't affect the sets that are the test subjects
print("This is the merging test")
odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}
u = even.union(odd)
print(u)
print("This is  the intersection")
print(odd.intersection(prime))
print("This is the difference")
print(odd.difference(prime))
print("This is double difference")
print(odd.symmetric_difference(prime))
# Note:There is an update way to change sets while merging and the things you see above
print("This is the update prove by intersection update")
odd.intersection_update(prime)
print(odd)
print("This was the value of odd now")
# This is the subset and superset function
set_1 = {1, 2, 3, 4, 5, 6, 7, 8}
set_2 = {1, 2, 3, 4, 5}
print(set_1.issubset(set_2))
print(set_2.issubset(set_1))
# "issuperset" is it's opposite function
# and this is the set copy helper

setA = {1, 2, 3, 4, 5, 6}
setB = setA

setB.discard(3)
print("This is setA")
print(setA)
print("this is setB")
print(setB)

# to solve this you can either use copy method or set method
# And there is also this frozen set, created by the frozen set method and it is immutable

freezer = frozenset([1, 2, 3, 4, 5, 6, 7])
print("This is frozen set")
print(freezer)