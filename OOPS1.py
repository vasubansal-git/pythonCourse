# Creating class

class Student:
    name = "Vasu Bansal"
    age = 19

#Creating object(instance of class)

s1 = Student()
print(s1)
print(s1.name, s1.age)

s2 = Student()
print(s2.name)


#Example:

class Car:
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)


#Constructor

# __init__ function is always executed when abject is initiated

class Member:

    #Default constructor
    def __init__(self):
        pass

    #Parameterized constructor    
    def __init__(self, fullName, age):
        # print(self)
        self.name = fullName
        self.age = age
        print("Add new member in Database...")

member1 = Member("Vasu", 19)
print(f"New member name is: {member1.name} \nage is: {member1.age}") 

member2 = Member("Karan", 25)
print(f"New member name is: {member2.name} \nage is: {member2.age}")

# We can add different methods in class

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print(f"Welcome Student: {self.name}")

    def getMarks(self):
        return self.marks
    
s1 = Student("Vasu", 97)
s1.welcome()
print(s1.getMarks())


#Practice
#Q1: Create a student class that takes name & marks of 3 subjects as an argument in constructor.Then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getAverage(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name} your Average score is: {sum/3:.2f}")


s1 = Student("Vasu", [99, 98, 56])
s1.getAverage()