def mystery_function(x, y):
    x = more_mystery(x) + more_mystery(y)
    return x

def more_mystery(x):
    return invert_number(x) + 3

def invert_number(number):
    return -1 * number

def main():
    num1 = int(input("enter any number: ")) # user types '1'
    num2 = int(input("enter another number: ")) # user types '3'
    num3 = mystery_function(num1, num2)
    print("your mystery number is: " + str(num3))

if __name__ == "__main__":
    main()
