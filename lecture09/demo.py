import sys
import os

# class example, which adds up all of the avovados sold
# per region within the year 2015
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

    input_file.close() # close the file

def main():
    if len(sys.argv) != 2:
        print("* ERROR: please provide a filename")
        exit(1)
    input_file = sys.argv[1]
    calculate_avocado_sales(input_file)

if __name__ == "__main__":
    main()
