#list is a collection which is ordered and changeable. Allows duplicate members.

names = ["Vasu", "Sarthak", "Ujjwal"]
marks = [3, 5, 6]
mix = [3, "Vasu", 5.9, True]

print(type(names))
print(names)

print(marks[0])
print(marks[1])

print(mix)

for i in names:
    print(i)

if 7 in marks:
    print("Yes")
else:
    print("No")

#list comprehension

lst = [i*i for i in range(10)]
print(lst)
lst1 = [i*i for i in range(10) if i%2 == 0]
print(lst1)

#question

lst2 = [i*i for i in range(2, 21) if i%2 == 0]
print(lst2)

#list methods ---------------------------------------------------------------------------------->

l = [1, 2, 3, 4, 5]
print(l)
l.append(6) #append() method adds an element at the end of the list
l.sort() #sort() method sorts the list ascending by default
l.sort(reverse = True) #sort() method sorts the list in descending order
l.reverse() #reverse() method reverses the elements of the list
print(l.index(1)) #index() method returns the index of the first occurrence of the specified value
print(l.count(3)) #count() method returns the number of elements with the specified value
m = l #it is a wrong way of copying a list
m = l.copy() #correct way of copying a list
m[0] = 0
print(m)
l.insert(1, 899) #insert() method inserts an element at the specified position
m = [900, 1000, 1100]
l.extend(m) #m ko kholo or l ke end me dal do

#question: calculate the product of all elements in the list
product = 1
for i in l:
    product = product * i
    i = i + 1
print(product)