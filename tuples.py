#tuples: immutable sequences of elements.

tup = (1, 5, 6, "Vasu", True)
tup1 = (1, ) #to create a tuple with single element, comma is necessary
print(type(tup), tup)
print(type(tup1), tup1) #it is not a tuple
print(tup[0]) #indexing
print(tup[1])
print(tup[2])
print(tup[3])

print(tup[-1]) #negative indexing
print(tup[-2])
print(tup[-3])

print(tup[0:])
print(tup[0:5:2])
print(tup[1:4]) #slicing

if "Vasu" in tup:
    print("Yes, Vasu is present in tuple")