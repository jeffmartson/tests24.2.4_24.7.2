# test_calculator.py
import pytest
from app.calculator import Calculator

# Создаем экземпляр калькулятора для каждого теста
@pytest.fixture
def calculator():
    return Calculator()

# Позитивный тест для метода умножения
def test_multiply(calculator):
    result = calculator.multiply(3, 2)
    assert result == 6

# Позитивный тест для метода деления
def test_division(calculator):
    result = calculator.division(6, 2)
    assert result == 3.0

# Позитивный тест для метода вычитания
def test_subtraction(calculator):
    result = calculator.subtraction(5, 2)
    assert result == 3

# Позитивный тест для метода сложения
def test_adding(calculator):
    result = calculator.adding(3, 2)
    assert result == 5

# Дополнительные позитивные тесты

# Позитивный тест для умножения чисел с плавающей точкой
def test_multiply_float(calculator):
    result = calculator.multiply(2.5, 3.5)
    assert result == 8.75

# Позитивный тест для деления чисел с плавающей точкой
def test_division_float(calculator):
    result = calculator.division(8.5, 2)
    assert result == 4.25

# Позитивный тест для вычитания отрицательных чисел
def test_subtraction_negative(calculator):
    result = calculator.subtraction(-5, -2)
    assert result == -3

# Позитивный тест для сложения отрицательных чисел
def test_adding_negative(calculator):
    result = calculator.adding(-3, -2)
    assert result == -5
