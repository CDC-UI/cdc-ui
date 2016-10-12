#!/usr/bin/env python
# ^ This is how linux (and possibly Darwin[OSX]) knows it's a Python script, allowing you to do "./intro.py"
# Windows uses the file extension

# from michael import switch

print 'Python says: "Hi, how are you today?"'


# Function definition
def example():
    """ This is an example function. """
    pass  # Do nothing, equivalent to { } in C/C++

# def           Tells python you're defining a function
# example       Name of the function
# :             Start of a statement (in this case, a function definition statement)
# ()            Function arguments (no arguments in this case)
# """ blah """  Multi-line comment, known as a "docstring"
# pass          Expression that does nothing

def wrapper_function(f):
    def wrapper():
        f(blah)
        return
    return wrapper

# Functions must be defined before using them, so the following line wouldn't be valid
# examine_artifact('C:\lol')
@wrapper_function
def examine_artifact(artifact):
    import os
    from os import path  # From the OS library, import the path sub-module
    return path.basename(artifact)  # Function call to os.path.basename, with the argument artifact


# File I/O
with open("virus.txt", "r") as infectedFile:
    virus = infectedFile.readlines()  # Reads lines of text from the file, returning a list object with the lines 

# with          Ensures the file object is closed when scope of the statement is left
# open          Opens the file "virus.txt" as read-only ("r")
# as            Makes infectedFile the opened file object

# Wait a second...where's the type?
# In Python, there are types, but they're dynamically determined at runtime (known as "duck typing")
# This allows some really cool stuff, but as with C, can be potentially dangerous if you're not careful
print type(virus)
print str(virus)
print type(str(virus))

# For loops over objects
# In this case, virus is a "list" object
# The for loop queries the object for each item, until it's out of objects
for a in virus:
    print a

for a in "string":
    print a


# Iterative for loop
for i in range(0, 5):
    print i**2


# List comprehension
a = [i for i in range(0, 500, 100)]  # Generates a list of numbers using the for loop
print a

# The previous code was rather pointless however, when you can do this...
b = range(0, 100, 10)
print b

# Adding two lists to create a new list
huh = a + b
print huh

# Print a sorted copy of the list object
print sorted(huh)

# Sort the list itself
huh.sort()
print huh

# String slicing (aka magic)
string = "Hackers <3 Python"
print string[0]         # 1st character
print string[-1]        # Last character
print string[-2]        # Second to last character
print string[:7]        # Everything up to the 8th character
print string[:4]        # Everything up to the 4th character
print string[8:10]      # 9th through 11th characters
print string[3:14:3]    # Every 3 characters from 3rd to 14th character

# Printing a string backward
lol = 'eminem'
print lol
print lol[::-1]

# Note we can use "" or '' for strings. Use whichever you want, unless you have ' or " in the string.
hello = '"Hello!"'
hello1 = "'Hello'"
''
""
""
''
print hello

# Strings are lists of characters, so you can sort them!
print sorted(string)


# You don't need a main. They are a good practice, however, to prevent overriding ("globbing") your global namespace
def main():

    # Function call on every object (in this case, a string) in a list
    for artifact in virus:
        print examine_artifact(artifact)

    # Function pointers
    a_function = examine_artifact  # Note the lack of ()
    for artifact in virus:
        print a_function(artifact)

    # Docstrings
    print example.__doc__
    print __doc__

    # Method inspection
    print example.__name__

    # Eval evaluates strings as Python expressions. 
    # So, if you have a file with python code or data types, you can run it as if it were a part of your program.
    with open("python_virus.txt", "r") as seriousFile:
        temp = seriousFile.readlines()
        for t in temp:
            print eval(t)

    # Also, you can define a function wherever you please
    def rogue():
        print "I'm a rogue function!"

    rogue()

# __name__ is the label for the currently executing file. 
# If it is the file that we begin executing from, that name is __main__
# Otherwise, it would be intro
# This is useful for testing classes/functions defined in other files independantly from the rest of the code
if __name__ == '__main__':
    main()
    # The following line, will error
    # rogue()
