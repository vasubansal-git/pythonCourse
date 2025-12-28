# String slicing 

"""
name = "Vasu bansal"
print(len(name))  # length of string
print(name[0:]) #all printed
print(name[:]) #all printed
print(name[0:5]) #Vasu  (5-1=4)

print(name[1:4]) #asu (4-1=3)
print(name[:4]) #Vasu (4-1=3)

#negative slicing
print(name[0:-3]) #Vasu ban ( -3 means last 3 char are excluded)
print(name[-1:-3]) # blank ( -1 means last char and -3 means 3rd last char are excluded)
print(name[-3:-1]) #sa ( -3 means 3rd last char and -1 means last char are excluded)

#quiz
nm = "Harry"
print(nm[-4:-2]) #ar

"""

#string 
#Strings are immutable (unchangeable) in nature.

a = "Vasu"
b = "Vasu!!!!!!!!!!!!!!"
c = "!!!!!Vasu!!!!! !!!!!!!!!! Sarthak"
print(len(a))
print(a.upper())
print(a.lower())

print(b.rstrip("!")) #rstrip() removes the trailing characters (characters at the end of a string)
print(a.replace("Vasu", "Sarthak"))

print(c.split(" ")) #split() method splits a string into a list.

blogHeading = "Introduction tO Python"
print(blogHeading.capitalize()) #capitalize() method converts the first character of a string to uppercase (if it is a letter).

str1 = "Welcome to the console!!!"
print(len(str1))
str2 = str1.center(50) #center() method returns a centered string.
print(len(str2))
print(str2)

print(a.count("a")) #count() method returns the number of occurrences of a substring in the given string.

print(blogHeading.endswith("Python")) #True

content = "This is a sample content with several words. This content is for testing."
print(content.endswith("is", 0, 7)) #True

print(content.find("is")) #2  (find() method returns the lowest index of the substring if it is found in given string. If it's not found then it returns -1)