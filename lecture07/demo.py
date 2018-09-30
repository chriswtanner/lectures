# task 2
cm_per_inch = 2.54
pounds_per_kilo = 2.2

def calculate_health(weight, height, age, name, act_level):
    # task 3
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
        + str(dri_male) + " calories. If you are a woman, your Basic Metabolic Rate "\
        + "is " + str(female_bmr) + " and your Daily Recommended Intake is " \
        + str(dri_female) + " calories.\n")

def main():
    # reads input file
    input_file = open('office.csv', 'r')
    for line in input_file:
        name, sex, height, age, weight, act_level = line.rstrip().split(',')
        height = float(height)
        age = int(age)
        weight = float(weight)
        act_level = int(act_level)
        calculate_health(weight, height, age, name, act_level)

    input_file.close()

if __name__ == "__main__":
    main()
