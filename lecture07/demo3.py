# task 2
cm_per_inch = 2.54
pounds_per_kilo = 2.2

def calculate_health(name, sex, height, weight, age, act_level):
    weight_kilos = weight / pounds_per_kilo
    height_cm = height * cm_per_inch
    bmr = -1
    dri = -1
    if sex == "m":
        bmr = (10 * weight_kilos + 6.25 * height_cm - 5 * age + 5)
        dri = bmr * (1.2 + .175 * act_level)
    elif sex == "f":
        bmr = (10 * weight_kilos + 6.25 * height_cm - 5 * age - 161)
        dri = bmr * (1.2 + .175 * act_level)
    else:
        print("Sorry, unfortunately we only know how to calculate stats on" \
            + " a gender-bindary system (m or f)")
        exit(1)

    print("Dear " + name + ", you are " + str(height_cm) \
        + " cm tall. Your weight is " + str(weight_kilos) \
        + " kilos. Your Basic Metabolic Rate is " + str(bmr) \
        + " and your Daily Recommended Intake is " + str(dri) \
        + " calories.")

def main():
    input_file = open('office.csv', 'r')
    for line in input_file:
        name, sex, height, age, weight, act_level = line.rstrip().split(',')
        sex = sex.lower()
        height = float(height)
        age = int(age)
        weight = float(weight)
        act_level = int(act_level)
        calculate_health(name, sex, height, weight, age, act_level)
    input_file.close()

if __name__ == "__main__":
    main()