# pass by reference:

# class Customer:

#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# def greet(customer):
#     if customer.gender == "Male":
#         print("Hello",customer.name,"sir")
#     else:
#         print("Hello",customer.name,"Ma'am")

# cust = Customer("vani","Female")
# # print(cust.name)

# greet(cust)

#Example: 

# class Customer:

#     def __init__(self, name):
#         self.name = name

# def greet(customer):
#     print(id(customer))

# cust = Customer("vasu")
# print(id(cust))

# greet(cust)

# Collection of Objects:---------------------------------------------------------------------->

# class Customer:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def intro(self):
#         print(f"I am {self.name} and i am {self.age} years old")

# c1 = Customer('Vasu', 20)
# c2 = Customer('Ankit', 24)
# c3 = Customer('Vani', 17)

# l = [c1, c2, c3]

# for i in l:
#     i.intro()

# Static variable and methods ----------------------------------------------------------------->
# If we need a same variable for different objects then we use static variable otherwise use instance variable.

class Atm:

    # static variable/class variable
    __counter = 1
    def __init__(self): # Constructor / Magic method

        # This is not a good practice. Anyone can update this variables
        # So make this variable private! with the use of (__)
        # self.pin = ""
        # self.balance = 0

        # instance variable:
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.counter
        Atm.__counter = Atm.__counter + 1

        print(id(self)) # to check address of self
        # self.__menu()

    # getter/Setter
    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("Pin changed")

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allowed")

    def __menu(self):
        user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposite
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
        """)

        if(user_input == "1"):
            self.create_pin()
        elif(user_input == "2"):
            self.deposite()
        elif(user_input == "3"):
            self.withdraw()
        elif(user_input == "4"):
            self.check_balance()
        else:
            print("Bye!")

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin set successfully")

        self.__menu()

    def deposite(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount
            print("Deposite successful")
        else:
            print("Invalid pin!")

        self.__menu()

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin!")

        self.__menu()

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(f"Your balance: {self.__balance}")
        else:
            print("Invalid pin!")

        self.__menu()

sbi = Atm()