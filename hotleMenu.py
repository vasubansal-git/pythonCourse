# Define the menu of restaurant.

menu = {
    'Pizza' : 80,
    'Pasta' : 85,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80,
}

# Greet
print("Welcome to HARYANA Restaurant")
print("Pizza: Rs 80\nPasta: Rs 85\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80\n")

orderTotal = 0 #80 + 85 = 165.

while True:
    item = input("Enter the name of the item you want to order: ")
    if (item == 'exit'):
        break

    if(item in menu):
        orderTotal += menu[item]
        print(f"Your item {item} has been ordered")
    else:
        print(f"Ordered item {item} is not available yet!")

print(f"The total amount of your orders to pay is {orderTotal}")
print("Thank you for visiting!")
