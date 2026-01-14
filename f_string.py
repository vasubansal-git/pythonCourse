letter = "My name is {0} and I am from {1}."
country = "India"
name = "Vasu"
formatted_string = letter.format(name, country)
print(formatted_string)

#f-strings: formatted string literals (Python 3.6+)
print(f"We use f-strings like this: My name is {{name}} and I am from {{country}}.")

print(f"Hey my name is {name} and I am from {country}.")

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49.09999999))

price = 49.09999999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(type(f"{2 + 3}"))  #expression inside f-string

#questions:

num = 123
print(f"{num:05d}") #output: 00123 (total width 5, padded with zeros)

#conditions inside f-strings
age = 18
print(f"You are {'an adult' if age >= 18 else 'a minor'}.")

marks = 85
print(f"You have {'Passed' if marks >= 40 else 'Failed'} in the exam with {marks} marks.")

