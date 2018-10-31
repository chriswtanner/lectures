import sys

# this program is the example that i walked us through in class
# the only difference is that i improved the names of some functions and
# variables so that it's more clear
# e.g., python in_class_examples.py OfficeScriptNewGirl.txt

# creates a list of the even #s from 0-99
def lists_example():
    list = []
    for i in range(0,100):
        if i % 2 == 0:
            list.append(i)

# opens the file (whose filename is passed-in) and returns its words as a list
def get_list_of_words(filename):
    input_file = open(filename, 'r')
    list_of_all_words = input_file.read().replace("\n", "").lower().split(" ")
    return list_of_all_words

# takes 2 inputs:
# (1) 'keyword'  (e.g., 'paper') represents a word that we're looking for
# (2) 'list_of_words' represents the document's contents as a list of words
# the function counts how many times the 'keyword' appears in the 'list_of_words'
def count_words(keyword, list_of_words):
    current_count = 0
    for i in list_of_words:
        if i == keyword:
            current_count += 1
    return current_count

# returns a dictionary of how many times each word appears in passed-in file
def get_word_counts(filename):

    # reminder: dictionaries store key -> value
    # here, our 'word_counts' dictionary will store:
    # key: word
    # values: # of times that word appears in the document
    word_counts = {}

    input_file = open(filename, 'r')
    list_of_all_words = input_file.read().replace("\n", "").lower().split(" ")
    for word in list_of_all_words:
        if word in word_counts.keys():
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1

    return word_counts

# the main() function of the program, which houses all higher-order executions
def main():

    # calls our list_example function
    lists_example()

    # creates a list of words from the filename "OfficeScriptPilot.txt"
    list_of_words = get_list_of_words("OfficeScriptPilot.txt")

    keywords = ["paper", "jim", "lunch", "dwight", "meeting"]

    # iterates through each of the keywords, so that we can call
    # our function which counts how many times it appears in
    # our 'words_in_file' list
    for keyword in keywords:
        num_times_appeared = count_words(keyword, list_of_words)
        print(keyword + " appeared " + str(num_times_appeared) + " times")

    # NOTE: instead of iterating through our 'keywords' list, we could have just
    # explicitly called our function for any word we were curious about
    num_times_appeared = count_words("pam", list_of_words)
    print("btw, pam appeared " + str(num_times_appeared) + " times")

    num_times_appeared = count_words("desk", list_of_words)
    print("btw, desk appeared " + str(num_times_appeared) + " times")

    num_times_appeared = count_words("call", list_of_words)
    print("btw, call appeared " + str(num_times_appeared) + " times")

    # ensures the user input an argument that specifies the file we should use
    if len(sys.argv) != 2:
        print("* ERROR: please specify a filename")
        exit(1)

    filename = sys.argv[1]

    # gets the word counts for a given file
    word_counts = get_word_counts(filename)

    # the following code, when uncommented, prints how many times each word appears
    '''
    for word in word_counts:
        print(word + " appears " + str(word_counts[word]))
    '''

if __name__ == "__main__":
	main()
