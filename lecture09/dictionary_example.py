import sys
import os

# class example, which adds up all of the avocados sold
# per region within the year 2015, then displays all of
# the values, along w/ the region which had the most sold
def calculate_avocado_sales(filename):

    # ensures the file exists
    if not os.path.exists(filename):
        print("* ERROR: " + filename + " does not exist")
        sys.exit()

    # initializes our dictionary
    num_sold_per_region = {}

    # the file exists, so let's open it!
    input_file = open(filename, 'r')
    input_file.readline()
    for line in input_file:
        columns = line.rstrip().split(";")
        region = columns[4]
        year = int(columns[3])
        num_sold = float(columns[2])

        # checks if the year is 2015 and we want to ignore lines of data
        # which have the region listed as 'TotalUS'
        if year == 2015 and region != "TotalUS":

            # checks if the key already exists, which implies we've already
            # set a value for it, so let's just update its value
            if region in num_sold_per_region:
                num_sold_per_region[region] = num_sold_per_region[region] + num_sold
            else: # means key doesn't exist yet, so let's start the count for it
                num_sold_per_region[region] = num_sold

    input_file.close() # close the file

    # iterates through the dictionary's keys, while
    # (1) printing the amount sold per region; and
    # (2) calculating which region sold the most
    max_sold = 0
    max_region = ""
    for region in num_sold_per_region:
        print(region + " sold " + str(num_sold_per_region[region]))

        # checks if the region sold more than our current most
        if num_sold_per_region[region] > max_sold:

            # updates the new highest value
            max_sold = num_sold_per_region[region]

            # updates which region has the new highest value
            max_region = region

    print("\nsummary:\n------------------------")
    print(max_region + " sold the most: " + str(max_sold))

def main():
    if len(sys.argv) != 2:
        print("* ERROR: please provide a filename")
        exit(1)

    calculate_avocado_sales(sys.argv[1])

if __name__ == "__main__":
    main()
