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
