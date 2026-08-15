# instance variable: variables in constructor is known as instance variable. Its value is different for different objects.

class Atm:
    def __init__(self): # Constructor / Magic method

        # This is not a good practice. Anyone can update this variables
        # So make this variable private! with the use of (__)
        # self.pin = ""
        # self.balance = 0

        self.__pin = ""
        self.__balance = 0

        print(id(self)) # to check address of self
        self.__menu()

    # getter/Setter
    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("Pin changed")

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

sbi = Atm() # reference variable = object

# Note: 
# Not any coder/Developer can access the private variable by updating.
# But if a coder update this (object._class__variable) then code will crash or currupt
# Nothing in python is truly private!