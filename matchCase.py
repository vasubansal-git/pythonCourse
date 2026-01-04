
x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Something else")



username = input("Enter your username: ")
password = input("Enter your password: ")

match (username, password):
    case ("admin", "1234"):
        print("Login successful")
    case ("admin", _):
        print("Wrong password")
    case (_, "1234"):
        print("Wrong username")
    case _:
        print("Wrong username and wrong password")