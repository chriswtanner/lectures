import re
import random
def main():


    text = "Code didn't work, no idea why..."
    pattern = 'o'
    matched_items = re.findall(pattern, text)
    print(matched_items)


    '''
    # EXAMPLE #1: find all text that matches a pattern
    tweet = "RT @jleicole For #WHD2013, I ran 5.312 @CharityMiles to help @GirlUp educate girls in the developing world. #EveryMileMatters #BeyGood"
    # the pattern is defined as:
    # starting w/ a hashtag followed by any character
    # except , and space.  the + denotes being at least 1 character long
    pattern = "#[^, ]+"
    hashtags = re.findall(pattern, tweet)
    print(hashtags)


    # EXAMPLE #2: replace text that matches a pattern.
    # we replace the end punctuation with a single .
    sentence = "Ms. Smith, are you okay?!?  Please talk to me! Oh dear ..."
    # the | means or.  So, it can match the thing on the left of | or the right
    # the brackets [] means any of the given characters
    # the \s* means any whitespace (such as space) that appears 0 or more times
    # the \. means a period and the + means it must appear 1 or more times
    pattern = "[?!]+|\s*\.+"
    sentence = re.sub(pattern, '.', sentence)
    print(sentence)

    text = "Code didn't work, no idea why..."
    pattern = '[a-zA-Z]+'
    print(re.findall(pattern, text))

    text = "555-123-1234, 33-555-123-1234"
    pattern = '\d{3}-\d{3}-\d{4}'
    print(re.findall(pattern, text))

    user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    while (user_input == "rock" or user_input == "paper" or user_input == "scissors"):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("\t** You picked " + user_input + " and computer picked " + computer_choice)

        user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    print("Oh, you entered something else!")

    user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    while (user_input == "rock" or user_input == "paper" or user_input == "scissors"):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("\t** You picked " + user_input + " and computer picked " + computer_choice)

        user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    print("Oh, you entered something else!")
    '''
if __name__ == "__main__":
    main()
