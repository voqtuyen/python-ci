"""
Unit tests for the Calculator class.
"""

import pytest

from src.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    @pytest.fixture
    def calc(self):
        """Create a Calculator instance for testing."""
        return Calculator()

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        assert calc.add(2, 3) == 5
        assert calc.add(10, 20) == 30

    def test_add_negative_numbers(self, calc):
        """Test adding negative numbers."""
        assert calc.add(-5, -3) == -8
        assert calc.add(-10, 5) == -5

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        assert calc.add(2.5, 3.5) == 6.0
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        assert calc.subtract(10, 5) == 5
        assert calc.subtract(20, 8) == 12

    def test_subtract_negative_numbers(self, calc):
        """Test subtracting negative numbers."""
        assert calc.subtract(-5, -3) == -2
        assert calc.subtract(5, -3) == 8

    def test_subtract_floats(self, calc):
        """Test subtracting floating point numbers."""
        assert calc.subtract(5.5, 2.5) == 3.0
        assert calc.subtract(0.3, 0.1) == pytest.approx(0.2)

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(7, 8) == 56

    def test_multiply_negative_numbers(self, calc):
        """Test multiplying negative numbers."""
        assert calc.multiply(-3, 4) == -12
        assert calc.multiply(-5, -6) == 30

    def test_multiply_by_zero(self, calc):
        """Test multiplying by zero."""
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(0, 10) == 0

    def test_multiply_floats(self, calc):
        """Test multiplying floating point numbers."""
        assert calc.multiply(2.5, 4) == 10.0
        assert calc.multiply(0.5, 0.5) == 0.25

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        assert calc.divide(10, 2) == 5
        assert calc.divide(15, 3) == 5

    def test_divide_negative_numbers(self, calc):
        """Test dividing negative numbers."""
        assert calc.divide(-10, 2) == -5
        assert calc.divide(-15, -3) == 5

    def test_divide_floats(self, calc):
        """Test dividing floating point numbers."""
        assert calc.divide(7.5, 2.5) == 3.0
        assert calc.divide(1, 3) == pytest.approx(0.333333, rel=1e-5)

    def test_divide_by_zero(self, calc):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_power_positive_numbers(self, calc):
        """Test raising to positive powers."""
        assert calc.power(2, 3) == 8
        assert calc.power(5, 2) == 25

    def test_power_zero_exponent(self, calc):
        """Test raising to the power of zero."""
        assert calc.power(5, 0) == 1
        assert calc.power(100, 0) == 1

    def test_power_negative_exponent(self, calc):
        """Test raising to negative powers."""
        assert calc.power(2, -1) == 0.5
        assert calc.power(10, -2) == 0.01

    def test_power_fractional_exponent(self, calc):
        """Test raising to fractional powers."""
        assert calc.power(4, 0.5) == 2.0
        assert calc.power(27, 1 / 3) == pytest.approx(3.0)

    def test_modulo_positive_numbers(self, calc):
        """Test modulo operation with positive numbers."""
        assert calc.modulo(10, 3) == 1
        assert calc.modulo(15, 4) == 3

    def test_modulo_negative_numbers(self, calc):
        """Test modulo operation with negative numbers."""
        assert calc.modulo(-10, 3) == 2
        assert calc.modulo(10, -3) == -2

    def test_modulo_floats(self, calc):
        """Test modulo operation with floating point numbers."""
        assert calc.modulo(7.5, 2.5) == pytest.approx(0.0)
        assert calc.modulo(10.5, 3) == pytest.approx(1.5)

    def test_modulo_by_zero(self, calc):
        """Test that modulo by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot perform modulo with zero divisor"):
            calc.modulo(10, 0)

    def test_edge_case_very_large_numbers(self, calc):
        """Test operations with very large numbers."""
        assert calc.add(1e10, 1e10) == 2e10
        assert calc.multiply(1e6, 1e6) == 1e12

    def test_edge_case_very_small_numbers(self, calc):
        """Test operations with very small numbers."""
        assert calc.add(1e-10, 1e-10) == pytest.approx(2e-10)
        assert calc.multiply(1e-5, 1e-5) == pytest.approx(1e-10)
