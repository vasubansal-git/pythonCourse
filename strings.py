#string: Anything you enclose between single and double quotes is considered as a string.
# String is essentially a sequence of array of textual data.
#Strings are used when working with unicode chracters and text.

name = "Vasu"
friend = "Sarthak"
onother_friend = "Ujjwal"

print("Hello", name)

#indexing

print(name[0]) #V
print(name[1]) #a
print(name[2]) #s
print(name[3]) #u
# print(name[4]) #indexerror(index out of range)

print("Let's use a for loop")
for i in name:
    print(i)


