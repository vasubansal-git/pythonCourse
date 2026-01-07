# #Match case

# x = int(input("Enter the value of x: "))
# match x:
#     case 0:
#         print("Zero")
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case _:
#         print("Something else")



# username = input("Enter your username: ")
# password = input("Enter your password: ")

# match (username, password):
#     case ("admin", "1234"):
#         print("Login successful")
#     case ("admin", _):
#         print("Wrong password")
#     case (_, "1234"):
#         print("Wrong username")
#     case _:
#         print("Wrong username and wrong password")

#combine match statements

# day = int(input("Enter the day: "))
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Today is a weekday")
#     case 6 | 7:
#         print("Today is a weekend")
#     case _:
#         print("Invalid day")

# combine match with if statements as guards

month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day(1-31): "))

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("January")
    case 1 | 2 | 3 | 4 | 5 if month == 2:
        print("February")
    case 1 | 2 | 3 | 4 | 5 if month == 3:
        print("March")
    case _:
        print("Invalid day or month")