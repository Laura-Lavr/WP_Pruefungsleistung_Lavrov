def bmi(weight, height):
    return weight/height**2


def calories(sex, age, height, weight, PAL):
    if sex == 'male':
        calories = 66.47 + (13.7 * weight) + (5 * height)-(4.7 * age) * int(PAL)
        return calories
    else:
        calories = 655.2 + (9.6 * weight) + (1.8 * height) - (4.7 * age) * int(PAL)
        return calories
