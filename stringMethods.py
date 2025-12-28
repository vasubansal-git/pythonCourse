# String slicing 

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
