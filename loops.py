#for loop:

names = ["Vasu", "Sarthak", "Rekha", "Neeraj", "Vani"]
for name in names:
    print(name)

for name in names:
    print(name)
    for i in name:
        print(i)

for i in range(5):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

#reverse loop
for i in range(10, -1, -1):
    print(i)


#while loop:

i = 0
while i < 5:
    print(i)
    i = i + 1

i = 0
while i <= 38:
    i = int(input("Enter a number: "))
    print("You entered:", i)

#decrementing while loop:

i = 5
while i > 0:
    print(i)
    i = i - 1
else:
    print("I am inside else")

#print square of numbers from 1 to 10:

i = 1
while i <= 10:
    print("Square of", i, "is", i * i)
    i = i + 1