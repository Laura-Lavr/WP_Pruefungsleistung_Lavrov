import pytest
from bmi_calories import calculate_bmi, calculate_calories, calculate_ffmi


@pytest.mark.parametrize('weight, height, expected_bmi, expected_category', [
    (70, 170, 24.22, 'Normalgewicht'),  # Normal BMI
    (50, 160, 19.53, 'Normalgewicht'),  # Underweight BMI
    (90, 180, 27.78, 'Übergewicht'),    # Overweight BMI
    (100, 160, 39.06, 'Adipositas')])   # Obese BMI
def test_bmi(weight, height, expected_bmi, expected_category):
    bmi, category = calculate_bmi(weight, height)
    assert bmi == expected_bmi
    assert category == expected_category


@pytest.mark.parametrize('sex, age, height, weight, PAL, expected', [
    ('male', 25, 180, 70, 1.2, 2107),   # Sedentary male
    ('female', 30, 165, 60, 1.55, 2150),  # Moderately active female
    ('male', 40, 175, 80, 1.9, 3354),   # Very active male
    ('female', 22, 160, 55, 1.2, 1641)])  # Sedentary female
def test_calories(sex, age, height, weight, PAL, expected):
    assert calculate_calories(sex, age, height, weight, PAL) == expected


@pytest.mark.parametrize('sex, weight, bodyfat, height, expected_ffmi, expected_category', [
    ('male', 70, 15, 175, 19.73, 'eine durchschnittliche Muskelmasse'),  # Normal case for male
    ('male', 80, 20, 180, 19.75, 'eine durchschnittliche Muskelmasse'),  # Higher weight and fat percentage for male
    ('male', 60, 10, 165, 20.75, 'eine überdurchschnittlich hohe Muskelmasse'),  # Lower weight and fat percentage for male
    ('male', 90, 25, 190, 18.09, 'wenig Muskelmasse'),  # Higher weight and higher fat percentage for male
    ('female', 70, 15, 175, 19.73, 'einen sehr muskulösen Körperbau'),  # Normal case for female
    ('female', 80, 20, 180, 19.75, 'einen sehr muskulösen Körperbau'),  # Higher weight and fat percentage for female
    ('female', 60, 10, 165, 20.75, 'die Obergrenze für natürlichen Muskelaufbau erreicht'),  # Lower weight and fat percentage for female
    ('female', 90, 25, 190, 18.09, 'einen sehr muskulösen Körperbau')  # Higher weight and higher fat percentage for female
])
def test_ffmi(sex, weight, bodyfat, height, expected_ffmi, expected_category):
    ffmi, category = calculate_ffmi(sex, weight, height, bodyfat)
    assert ffmi == pytest.approx(expected_ffmi, abs=0.01)
    assert category == expected_category