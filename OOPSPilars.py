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
