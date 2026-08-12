# Object Oriented Programming

# l = [1, 2, 3, 4]

# lUpper = l.upper()
# print(lUpper) # no attribute error occured



# city = "Shahabad"

# cityUpper = city.upper()
# print(cityUpper) #run perfectly


# Class ----------------------------------------------------------------------------->
# Class is a blueprint.
# 1. Data or property  2. Functions or behaviour


# a = 1 #variable/Object
# print(type(a))


# Class Basic structure: 
# Class name should be in Pascal case eg. ThisIsPascalCase


# class Car:
#     color = "blue" #data
#     model = "sports" #data

#     def calculate_avg_speed(km, time):
#         #some code


# Object ---------------------------------------------------------------------------------->
# Object is an instance of the Class

# Example:

# 1. Car---------------------->WagonR//  wagonr = Car()
# 2. Sports---------------------> Gilli Danda//  gillidanda = Sports()
# 3. Animals--------------------> Langoor//  langoor = Animals()

# Atm:

class Atm:
    def __init__(self): # Constructor
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
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
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")

    def deposite(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance = self.balance + amount
            print("Deposite successful")
        else:
            print("Invalid pin!")

    def withdraw(self):
            temp = input("Enter your pin: ")
            if temp == self.pin:
                amount = int(input("Enter the amount: "))
                if amount < self.balance:
                    self.balance = self.balance - amount
                    print("Withdraw successful")
                else:
                    print("Insufficient balance")
            else:
                print("Invalid pin!")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance: {self.balance}")
        else:
            print("Invalid pin!")

a = Atm() #calling