# example of:
# (1) how to use lists, namely:
#  - adding items to a list
#  - removing items from a list
#  - find the index of an item in the list
#  - sort the list
#  - reverse the list
# (2) use a for loop to iterate through a list
def starts_with_vowel(word):
    if word.startswith('a') or word.startswith('e') or word.startswith('i') \
    or word.startswith('o') or word.startswith('u'):
        return True
    else:
        return False

def main():
    names = [] # initializes a new, empty list
    names = ['a', 'b', 'c']
    names.insert(0, 'x')
    # add items to the list

    # remove an item from the list
    names.sort()
    print(names)
    # find an item in the list

    # sort the list

    # reverse the list

    # loop (iterate) through the list and call the function for each


if __name__ == "__main__":
    main()
