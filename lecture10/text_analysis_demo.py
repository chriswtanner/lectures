import sys
'''
def get_letter_dictionary(filename):
    return letter_to_words

def get_popular_words(word_counts):
    return popular_words

def get_word_counts(filename):
    return word_counts
'''
def main():
    # ensures user input an argument to specify that filename
    if len(sys.argv) != 2:
        print("* ERROR: please provide a filename and threshold value")
        exit(1)

    filename = sys.argv[1]

    word_counts = get_word_counts(filename)

    #popular_words = get_popular_words(word_counts)
    # get_letter_dictionary(filename)

if __name__ == "__main__":
    main()
