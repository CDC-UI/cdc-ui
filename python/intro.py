#!/usr/bin/env python

print 'Python says: "Hi, how are you today?"'


# Function definition
def example():
    """ This is an example function. """
    pass  # Do nothing, equivilent to { } in C/C++

# def           Tells python you're defining a function
# example       Name of the function
# :             Start of the statement (in this case, a function definition statement)
# ()            Arguments to the function (no arguments in this case)
# """ blah """  Multi-line comment. When placed inside the function (there is a tab or 4 spaces), it is the functions docstring
# pass          Expression that does nothing 

def examine_artifact(artifact):
    from os import path  # From the OS library, import the path sub-module
    return path.basename(artifact)  # Function call to os.path.basename, with the argument artifact


# File I/O
with open("virus.txt", "r") as infectedFile:
    virus = infectedFile.readlines()  # Reads lines of text from the file, returning a list object with the lines 

# with          Ensures the file object is closed when scope of the statement is left
# open          Opens the file "virus.txt" as read-only ("r")
# as            Assigns the result of the open to the variable infectedFile

# For loops over objects
for a in virus:
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

# Print a copy of the list object that is sorted
print sorted(huh)

# Sort the list itself
huh.sort()
print huh

# String slicing (aka magic)
string = "Hackers <3 Python"
print string[0]
print string[-1]
print string[:7]
print string[:4]
print string[8:10]
print string[3:14:3]

# Printing a string backward
lol = "eminem"
print lol
print lol[::-1]

# Strings are lists of characters, so you can sort them!
print sorted(lol)


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

# __name__ is the label for the currently executing file. 
# If it is the file that we begin executing from, that name is __main__
# Otherwise, it would be intro
# This is useful for testing classes/functions defined in other files independantly from the rest of the code
if __name__ == '__main__':
    main()
