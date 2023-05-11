import math
# Variable Scope
# Global Scope
g = 25

def main(args):
    # Local Scope
    x = 1
    
    # Call the arc_length function with only one argument
    # even though the arc_length function has two parameters.
    len1 = arc_length(4.7)
    print(f"len1: {len1:.1f}")

    # Call the arc_length function again but
    # this time with two arguments.
    len2 = arc_length(4.7, 270)
    print(f"len2: {len2:.1f}")


# Define a function with two parameters. The
# second parameter has a default value of 360.
def arc_length(radius, degrees=360):
    """Compute and return the length of an arc of a circle."""
    circumference = 2 * math.pi * radius
    length = circumference * degrees / 360
    return length

# Compress the function for reduce the number of lines 
def example(n):
    if n % 2 == 0:
        return True
    else: 
        return False
# Reduzing to ONE line
def example2(n):
    return True if n % 2 == 0 else False
# Reduzing more
def example3(n):
    return n % 2 == 0

# LEARNING ABOUT --------------MATCH------------------

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Newt":
        print("Luffa Luffa")


main()