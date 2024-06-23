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


def calculate_calories(sex, age, height, weight, PAL):
    if sex == 'male':
        grundumsatz = 66.47 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        grundumsatz = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    return round(grundumsatz * PAL)


def calculate_ffmi(sex, weight, height, bodyfat):
    lean_mass = weight * (1 - bodyfat / 100)
    height_m = height / 100
    ffmi = lean_mass / (height_m ** 2)
    ffmi_adjusted = ffmi + 6.1 * (1.8 - height_m)

    category = ''
    if sex == 'male':
        if ffmi_adjusted <= 18:
            category = 'sehr wenig Muskelmasse'
        elif 18 < ffmi_adjusted <= 19:
            category = 'wenig Muskelmasse'
        elif 19 < ffmi_adjusted <= 20:
            category = 'eine durchschnittliche Muskelmasse'
        elif 20 < ffmi_adjusted <= 22:
            category = 'eine überdurchschnittlich hohe Muskelmasse'
        elif 22 < ffmi_adjusted <= 24:
            category = 'einen sehr muskulösen Körperbau'
        elif 24 < ffmi_adjusted <= 25:
            category = 'die Obergrenze für natürlichen Muskelaufbau erreicht'
        else:
            category = 'einen Körper, der ohne Anabolika kaum zu erreichen ist'
    else:
        if ffmi_adjusted <= 13:
            category = 'sehr wenig Muskelmasse'
        elif 13 < ffmi_adjusted <= 14:
            category = 'wenig Muskelmasse'
        elif 14 < ffmi_adjusted <= 16:
            category = 'eine durchschnittliche Muskelmasse'
        elif 16 < ffmi_adjusted <= 18:
            category = 'eine überdurchschnittlich hohe Muskelmasse'
        elif 18 < ffmi_adjusted <= 20:
            category = 'einen sehr muskulösen Körperbau'
        elif 20 < ffmi_adjusted <= 21:
            category = 'die Obergrenze für natürlichen Muskelaufbau erreicht'
        else:
            category = 'einen Körper, der ohne Anabolika kaum zu erreichen ist'

    return round(ffmi_adjusted, 2), category