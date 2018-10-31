import sys
# this program demonstrates a few calculations with the text of a document
# the user should pass in a filename
# e.g., python text_analysis.py OfficeScriptNewGirl.txt
def get_letter_dictionary(filename):
    """ This function reads a file and gathers all the words that
    start with each letter

    Input arguments:
    filename -- the name of the file which we will open and operate on

    Returns:
    a dictionary which stores lists of words according to the letter
    they start with, e.g.:
    t -> [the, table, the, topic, thanks, ... ]
    b -> [boy, baseball, benevolent, ... ]
    c -> [creative, clever, capricious, ... ]
    """

    input_file = open(filename, 'r')

    # creates a list of words (lowercased) from the passed-in filename
    words = input_file.read().lower().replace('\n','').split(" ")

    letter_to_words = {} # initializes a dictionary

    # iterate through each word in our list of words
    for word in words:

        # ignore words that are only 1 letter in length
        if len(word) > 1:

            # gets the first letter of the word (a word is just a list of characters)
            first_letter = word[0]

            # checks if we already have a list of words for the given first_letter
            if first_letter in letter_to_words.keys():

                # grab the current list (aka the value)
                cur_list = letter_to_words[first_letter]
                cur_list.append(word) # append our word to it
                letter_to_words[first_letter] = cur_list # sets a new value

            # we haven't seen a word that starts w/ this 'first_letter', so let's
            # initialize a new list w/ the current word
            else:
                new_list = []
                new_list.append(word)
                letter_to_words[first_letter] = new_list

    return letter_to_words

    # returns a list of words that appear more than the passed-in threshold
def get_popular_words(word_counts, threshold):

    popular_words = []

    # iterates through each unique word (aka our keys)
    # and populates a list of the ones that have high occurrence counts
    for word in word_counts.keys():
        if word_counts[word] >= threshold:
            popular_words.append(word)
    return popular_words

def get_word_counts(filename):
    """ This function counts how many times
    each word appears in the passed-in file

    Keyword arguments:
    filename -- the name of the file which we will open and operate on

    Returns:
    a dictionary which stores how many times each word occurs in the file
    """
    input_file = open(filename, 'r')

    # creates a list of words (lowercased) from the passed-in filename
    words = input_file.read().lower().replace('\n','').split(" ")

    word_counts = {} # will store how many times each word occurs

    # iterates through each word in the list of words
    for word in words:
        if word in word_counts.keys():
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1

    return word_counts

def main():
    if len(sys.argv) != 2:
        print("* ERROR: please provide a filename")
        exit(1)

    filename = sys.argv[1]

    word_counts = get_word_counts(filename)

    # returns a list of all words that appeared more than 100 times
    popular_words = get_popular_words(word_counts, 100)
    print("popular_words: " + str(popular_words))

    letter_to_words = get_letter_dictionary(filename)
    print("y words: " + str(letter_to_words['y']))

if __name__ == "__main__":
    main()
