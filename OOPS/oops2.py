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

class Customer:

    def __init__(self, name):
        self.name = name

def greet(customer):
    print(id(customer))

cust = Customer("vasu")
print(id(cust))

greet(cust)