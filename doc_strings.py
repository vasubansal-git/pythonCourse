#Python docstrings are the string literals that appear right after the defination of a function, method, class, or module.
#This is totally different from comments bcoz when we change the comments there is no effect on the output but 
# when we change the doc string there we can see the effect on output.  
def square(n):
    '''Takes in a number n, returns the square of n.'''
    square = n * n
    return square

print(square.__doc__)
print(square(9))