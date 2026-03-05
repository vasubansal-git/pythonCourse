def welcome():
    print("Hi, Welcome to the world of python")

print(__name__)

if __name__ == "__main__": #ab ik baar hi chlega isko yhin se run kiya jara hai to welcome ko execute krenge
    welcome()

# ------------------------------------------------------------------------------------------------------ 

def add(a, b):
    return a + b

print("This is alway executed")

print(__name__)

if __name__ == "__main__":
    result = add(5, 6)
    print("Result: ", result)