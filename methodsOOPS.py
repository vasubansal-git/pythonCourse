class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #decorator
    def hello():
        print("Hello")

    def getAvg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is: ", sum/3)

s1 = Student("Vasu", [89, 90, 95])
s1.getAvg()
s1.hello()