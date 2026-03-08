# REASING A FILE

f = open('first.txt', 'r')
txt = f.read()
print(txt)
f.close()

# WRITING A FILE

f = open('IO.txt', 'a')
# f.write('Hello, vasu')
f.write(' Eerything is fine')
f.close()

f = open('IO.txt', 'r')
txt = f.read()
print(txt)
f.close()

# with

with open('IO2.txt', 'w') as f:
    f.write('Hey I am inside the file by with keyword')