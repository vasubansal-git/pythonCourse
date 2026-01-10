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