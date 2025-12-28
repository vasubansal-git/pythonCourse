a1 = "1" #string
b1 = "2" #string

a2 = 1 #int
b2 = 2 #int

print(a1 + b1) #12
print(int(a1) + int(b1)) #3 Explicit typecasting

print(a2 + b2) #3
print(str(a2) + str(b2)) #12

#Explicit typecasting

string = "15"
number = 7

string_number = int(string)
sum = string_number + number
print("The sum is:", sum)

#Implicit typecasting

c = 1.9
d = 8
print(c + d)

e = 7
print(type(e)) #int

f = 3.0
print(type(f)) #float

g = e + f
print(g)
print(type(g)) #float
