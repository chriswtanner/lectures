import re
def main():

    # TASK 1
    # 1. "[aeiou]v"
    # 2. "[h(ae)]*"
    # 3. ".*\.\s+.*"

    text = input("enter it:" ) #"who are you?!  (it's me)"
    cleaned = re.sub('[!?\.,\_\;\/\)\(\\\]', '', text)
    print(cleaned)
    #[hae]*"

    #matched_items = re.findall(pattern, text)
    #print(matched_items)

if __name__ == "__main__":
    main()
