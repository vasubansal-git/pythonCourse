# Inheritance Examples:

#------------------------------------------------------ Inheriting Constructor -----------------------------------------------------

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "Samsung", 30)
print(s.brand)

# ----------------------------------------------------- Inheriting private members ------------------------------------------------

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "Samsung", 30)
print(s.__brand)