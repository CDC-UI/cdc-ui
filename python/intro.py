#!/usr/bin/env python

print 'Python says: "Hi, how are you today?"'


# Function definition
def example():
    """ This is an example function. """
    pass  # Do nothing


def examine_artifact(artifact):
    from os import path
    return path.basename(artifact)


# File I/O
with open("virus.txt", "r") as infectedFile:
    virus = infectedFile.readlines()


# For loops over objects
for a in virus:
    print a


# Iterative for loop
for i in range(0, 5):
    print i**2

# List comprehension
huh = [i for i in range(0, 500, 100)]
print huh


# String slicing (aka magic)
string = "Hackers <3 Python"
print string[0]
print string[-1]
print string[:7]
print string[:4]
print string[8:10]
print string[3:14:3]

lol = "eminem"
print lol
print lol[::-1]


# You don't need a main. They are a good practice, however, to prevent globbing your global namespace
def main():

    # Function calls
    for artifact in virus:
        print examine_artifact(artifact)

    # Function pointers
    a_function = examine_artifact
    for artifact in virus:
        print a_function(artifact)

    # Docstrings
    print example.__doc__

    # Method inspection
    print example.__name__

    # Eval
    with open("python_virus.txt", "r") as seriousFile:
        temp = seriousFile.readlines()
        for t in temp:
            print eval(t)

if __name__ == '__main__':
    main()
