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

#tuple methods ---------------------------------------------------------------------------------->

#mutation of tuple
countries = ("India", "USA", "UK", "Germany")
temp = list(countries) #convert tuple to list
temp.append("France") #mutate the list
temp[2] = "Finland"
countries = tuple(temp) #convert list back to tuple
print(countries)

#concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

res = t1.count(2) #count() method returns the number of occurrences of a specified value
print(res)

res1 = t3.index(5) #index() method returns the index of the first occurrence of a specified value
print(res1)

#unpacking
a, b, c = t1
print(a)
print(b)
print(c)

