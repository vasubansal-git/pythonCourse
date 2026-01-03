"""
a = int(input("Enter your age: "))
print("Your age is:", a)

#Conditional operators: >, <, >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")

"""

applePrice = 210
budget = 200
if(applePrice <= budget):
    print("Alexa, add 1kg apple to the cart")
else:
    print("Alexa, donot add apples to the cart")

#another code:
num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero")
else:
    print("Number is positive")

#nested if-else

num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is postive and in between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is positive and in between 11-20")
    else:
        print("Number is positive and greater than 20")
else:
    print("Number is zero")        



#Write a Python program that asks the user to enter their marks (0–100) and prints the grade according to the following rules:

#If marks are 90 or above, print "Grade: A"

#If marks are 80 to 89, print "Grade: B"

#If marks are 70 to 79, print "Grade: C"

#If marks are 60 to 69, print "Grade: D"

#If marks are below 60, print "Grade: F"

marks = int(input("Enter your marks(0-100): "))

if(marks >= 90 and marks <= 100):
    print("Grade: A")
elif(marks >= 80 and marks < 90):
    print("Grade: B")
elif(marks >= 70 and marks < 80):
    print("Grade: C")
elif(marks >= 60 and marks < 70):
    print("Grade: D")
else:
    print("Grade: F")