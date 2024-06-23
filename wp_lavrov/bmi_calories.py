def calculate_bmi(weight, height):
    bmi = round(weight / (height / 100) ** 2, 2)
    category = ''
    if bmi < 18.5:
        category = 'Untergewicht'
    elif 18.5 <= bmi < 24.9:
        category = 'Normalgewicht'
    elif 25 <= bmi < 29.9:
        category = 'Übergewicht'
    else:
        category = 'Adipositas'
    return bmi, category


def calories(sex, age, height, weight, PAL):
    if sex == 'male':
        grundumsatz = 66.47 + (13.7 * weight) + (5 * height)-(4.7 * age)
        return round(grundumsatz * PAL)
    else:
        grundumsatz = 655.2 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        return round(grundumsatz * PAL)


def calculate_ffmi(sex, weight, height, bodyfat):
    lean_mass = weight * (1 - bodyfat / 100)
    height_m = height / 100
    ffmi = round(lean_mass / (height_m ** 2), 2)
    ffmi_adjusted = round(ffmi + 6.1 * (1.8 - height_m), 2)
    category = ''
    if ffmi_adjusted <= 18 and sex == 'male' or ffmi_adjusted <= 13 and sex == 'female':
        category = 'sehr wenig Muskelmasse'
    elif 18 < ffmi_adjusted <= 19 and sex == 'male' or 13 < ffmi_adjusted <= 14 and sex == 'female':
        category = 'wenig Muskelmasse'
    elif 19 < ffmi_adjusted <= 20 and sex == 'male' or 14 < ffmi_adjusted <= 16 and sex == 'female':
        category = 'eine durchschnittliche Muskelmasse'
    elif 20 < ffmi_adjusted <= 22 and sex == 'male' or 16 < ffmi_adjusted <= 18 and sex == 'female':
        category = 'eine überdurchschnittlich hohe Muskelmasse'
    elif 22 < ffmi_adjusted <= 24 and sex == 'male' or 18 < ffmi_adjusted <= 20 and sex == 'female':
        category = 'einen sehr muskulösen Körperbau'
    elif 24 < ffmi_adjusted <= 25 and sex == 'male' or 20 < ffmi_adjusted <= 21 and sex == 'female':
        category = 'die Obergrenze für natürlichen Muskelaufbau erreicht'
    else:
        category = 'einen Körper, der ohne Anabolika kaum zu erreichen ist'
    return ffmi_adjusted, category

