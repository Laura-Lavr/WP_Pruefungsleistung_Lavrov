from bmi_calories import calculate_bmi, calories, calculate_ffmi
import pytest


@pytest.mark.parametrize('weight, height, expected', [
    (70, 170, 24),  # Normal BMI
    (50, 160, 20),  # Underweight BMI
    (90, 180, 28),  # Overweight BMI
    (100, 160, 39)])  # Obese BMI
def test_bmi(weight, height, expected):
    assert round(calculate_bmi(weight, height)) == expected


@pytest.mark.parametrize('sex, age, height, weight, PAL, expected', [
    ('male', 25, 180, 70, 1.2, 2170),   # Sedentary male
    ('female', 30, 165, 60, 1.55, 2150),   # Moderately active female
    ('male', 40, 175, 80, 1.9, 3514),   # Very active male
    ('female', 22, 160, 55, 1.2, 1641)])   # Sedentary female
def test_calories(sex, age, height, weight, PAL, expected):
    assert round(calories(sex, age, height, weight, PAL)) == expected


@pytest.mark.parametrize('weight, fat_percentage, height, expected', [
    (70, 15, 175, 19),  # Normal case
    (80, 20, 180, 20),  # Higher weight and fat percentage
    (60, 10, 165, 20),  # Lower weight and fat percentage
    (90, 25, 190, 19)])  # Higher weight and higher fat percentage
def test_ffmi(weight, fat_percentage, height, expected):
    assert round(calculate_ffmi(weight, fat_percentage, height)) == expected


