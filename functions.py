def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def largestNumber(a, b):
    if a > b:
        print(a, "is bigger")
    else:
        print(b, "is bigger")

def is_lesser(a, b):
    pass #interpreter will ignore this funtion and dont search for its implementation


a = 9
b = 8
# gmean = (a*b)/(a+b)
# print("Geometric Mean is:", gmean)
calculateGmean(a, b)
largestNumber(a, b)

c = 6
d = 4
# gmean = (c*d)/(c+d)
# print("Geometric Mean is:", gmean)
calculateGmean(c, d)
largestNumber(c, d)

#functions with arguments:

def average(a = 9, b = 1):
    print("The average is: ", (a + b)/2)

average() #default arguments will be taken
average(4, 6) #user defined arguments will be taken
average(5) #first argument will be user defined and second will be default(b = 1)

def average2(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    print("The average is: ", sum/len(numbers))

average2(4, 5, 6, 7, 8)