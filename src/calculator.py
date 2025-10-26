"""
A simple calculator module with basic arithmetic operations.
"""


class Calculator:
    """Calculator class with basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b.

        Args:
            a: The dividend
            b: The divisor

        Returns:
            The quotient of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Raise a to the power of b."""
        return float(a**b)

    def modulo(self, a: float, b: float) -> float:
        """
        Return the remainder of a divided by b.

        Args:
            a: The dividend
            b: The divisor

        Returns:
            The remainder of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero divisor")
        return a % b
