# global variables, which should only be used for accessing, never updating
cm_per_inch = 2.54
pounds_per_kilo = 2.2

# our function which calculates the bmr and dri
# for a given person based on their height, weight, age,
# and activity level, and we print the bmr and dri to the screen
def calculate_health(name, height, weight, age, act_level):
    weight_kilos = weight / pounds_per_kilo
    height_cm = height * cm_per_inch
    male_bmr = (10 * weight_kilos + 6.25 * height_cm - 5 * age + 5)
    female_bmr = (10 * weight_kilos + 6.25 * height_cm - 5 * age - 161)
    dri_male = male_bmr * (1.2 + .175 * act_level)
    dri_female = female_bmr * (1.2 + .175 * act_level)
    print("Dear " + name + ", you are " + str(height_cm) \
        + " cm tall. Your weight is " + str(weight_kilos) \
        + " kilos. If you are a man, your Basic Metabolic Rate is " \
        + str(male_bmr) + " and your Daily Recommended Intake is " \
        + str(dri_male) + " calories. If you are a woman, your Basic " \
        + "Metabolic Rate is " + str(female_bmr) + " and your Daily " \
        + "Recommended Intake is " + str(dri_female) + " calories.\n")

# main function for our higher-order code
def main():

    # reads input file
    input_file = open('office.csv', 'r')
    for line in input_file:
        name, sex, height, age, weight, act_level = line.rstrip().split(",")

        height = float(height)
        age = int(age)
        weight = float(weight)
        act_level = int(act_level)

        # calls our calculate_health() function, while passing it
        # the 5 necessary variables to work with
        calculate_health(name, height, weight, age, act_level)

    # closes the input_file
    input_file.close()

# this is the main entry point of our entire Python program
if __name__ == "__main__":
    main() # calls our main() function
