# polymorphism ---------------------------------------------------------------------------------------------------------------------

class Phone:

    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("BUying a phone")

class SmartPhone(Phone):

    def buy(self):
        print("Buying a smart phone")

s = SmartPhone(20000, "Samsung", 30)
s.buy()

# Method Overring -> polymorphism
# Method overloading
# Operator overloading

# ------------------------------------------------------------ Example 2 ----------------------------------------------

class A:

    def __init__(self):
        self.var1 = 100

    def display1(self,var1):
        print("class A:", self.var1)

class B(A):

    def display2(self,var1):
        print("class B:", self.var1)

obj = B()
obj.display1(200)

# ----------------------------------------------------- Example of super ------------------------------------------------------

class Phone:

    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying phone")

class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        super().buy()

s = SmartPhone(20000, "Samsung", 30)

s.buy()

# ----------------------------------------------------------- super example with constructor -----------------------------------

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smart phone constructor")

s = SmartPhone(20000, "Samsung", 30, "Android", 8)

print(s.os)
print(s.brand)