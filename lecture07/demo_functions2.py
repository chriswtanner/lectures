# this program is designed to just be an example of how functions are
# defined and how their variables are local to themselves.  that is,
# plus()'s inputs and outputs are the ONLY relation to other parts
# or other functions of our code.  plus()'s variables a, b, and c,
# are its own variables.  so, lines 11, 12, and 13 have no affect
# on main()'s variables w/ the same name (a, b, c), other than
# the fact that we set main()'s "c" to be equal to the output of plus()
# you should take the time to play w/ this example, try different things,
# add code, print out various variables and see what happens.
def plus(a, b):
    a = 2 * a
    b = 3 + b
    c = a + b
    return c

# main function for our higher-order code
def main():
    a = 3
    b = 5
    c = plus(a, b)
    c += 1
    print(a)
    print(b)
    print(c)

# this is the main entry point of our entire Python program
if __name__ == "__main__":
    main() # calls our main() function
