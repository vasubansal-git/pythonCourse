x = 4 # Global Variable
print(x)

def hello():
    x = 5 # Local Variable
    y = 10
    print(f"The local x is {x}")
    print("Hello, vasu")
    print(y)

print(f"The global x is {x}")
hello()
print(f"The global x ix {x}")
# print(y) #This will cause an error because y is a local variable and not accessible outside of the function.

# To solve this we can use global keyword in our function

z = 5 # Global Variable
print(z)

def test():
    global p
    p = 10 #Global Variable
    l = 14 # Local Variable
    print(l)

test()
print(f"The Global variable is {p}")
print(f"The Global variable is {z}")
# print(l) # This will cause an error