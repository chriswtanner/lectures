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

    # add items to the list
    names.append('arjun')
    names.append('nicole')
    names.append('cynthia')
    names.append('joelle')
    print(names)

    # add steve to beginning of list
    names.insert(0, 'steve')
    print(names)

    # remove steve from the list
    # Q1: what happens if we have multiple items named 'steve'?
    # which one does it remove?
    names.remove('steve')
    print(names)

    # find an item in the list
    index_found = names.index('joelle')
    print(index_found)

    # Q2: what happens if the value isn't found, such as searching for 'steve'?

    # sort the list
    names.sort()
    print(names)

    # reverse the list
    names.reverse()
    print(names)

    # loop (iterate) through the list and call the function for each
    for name in names:
        if starts_with_vowel(name):
            print(name + " starts w/ a vowel!")
        else:
            print(name +  " does NOT start w/ a vowel")

if __name__ == "__main__":
    main()
