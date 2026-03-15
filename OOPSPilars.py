# Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.cluch = True
        self.acc = True
        print("Car started..")

car1 = Car()
car1.start()

# Encapsulation: Wrapping data and functions into a single unit(object)

#practice:

#Q1. Create Account class with 2 attributes- balance and account no
#    Create method for debit, credit & printing the balance

class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(100000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(1000)

#del keyword: Used to delete object properties or object itself.

class student:
    def __init__(self, name):
        self.name = name

s1 = student("Vasu Bansal")
print(s1.name)

del s1
print(s1.name)

#Private attributes & methods
#Private attributes & methods are meant to be used only within the class ans are not accessible from outside the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def get_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.get_pass())
print(acc1.__acc_pass) #shows error

#Inheritance: When one class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.name)
print(car1.start())
print(car1.color)

#Multi-level inheritance

class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

#Multiple Inheritance:- ik hi derived class jb multiple classes ki properties le ske.

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

#super()

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    def stop():
        print("Car stopped..")

class ToyotoCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotoCar("pirus", "electric")
print(car1.type)


#class method: It is bound to the class & receives the class as an implicit first argument.
# Note: static method can't access or modify class state & generally for utility.

class person:
    name = "anonymous"

    # def changeName(self, name):
    #     # self.name = name
    #     person.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = person()
p1.changeName("Vasu Bansal")
print(p1.name)
print(person.name)


#property decorator: we use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

stud1 = Student(99, 88, 99)
print(stud1.percentage)

stud1.phy = 86
print(stud1.phy)
stud1.calcPercentage()
print(stud1.percentage)


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
    
stud1 = Student(98, 97, 99)
print(stud1.percentage)

stud1.phy = 86
print(stud1.percentage)


#Polymorphism: Operator Overloading
#When the same operator is allowed to have different meaning according to the context

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, comp2):
        newReal = self.real + comp2.real
        newImg = self.img + comp2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, comp2):
        newReal = self.real - comp2.real
        newImg = self.img - comp2.img
        return Complex(newReal, newImg)

comp1 = Complex(1, 3)
comp1.showNumber()

comp2 = Complex(4, 7)
comp2.showNumber()

#when dunder function is not exist
# comp3 = comp1.add(comp2)
# comp3.showNumber()

#When dunder function is exist
comp3 = comp1 + comp2
comp3.showNumber()

comp4 = comp1 - comp2
comp4.showNumber()


# PRACTICE -----------------------------------------------------------------------------------------------------------

#Q1. Define a circle class to create a circle with radius r using the constructor.
#    Define an Area() method of the class which calculates the area of the circle.
#    Define a Parimeter() method of the class which allows you to create the parimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(f"Circle area: {c1.Area()}")
print(f"Circle perimeter: {c1.perimeter()}")

#Q2.Define a Employee class with attributes role, department & salary. This class have showDetails() method.
#   Create an Engineer class that inherits properties from employee & add some other attributes: name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}")
        print(f"Dept: {self.dept}")
        print(f"Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

    def enggShowDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# e1 = Employee("Engineer", "CSE", 75000)
# e1.showDetails()

engg1 = Engineer("Vasu", "19")
engg1.enggShowDetails()
engg1.showDetails()

#Q3. Create a classs called Order which stores item & its price.
#    Use dunder function __gt__() to convey that:
#       order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price


order1 = Order("Chips", "20")
order2 = Order("Kurkure", "10")

print(order1 > order2)