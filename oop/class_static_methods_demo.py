class Calculator:
    """A class demonstrating static methods and class methods."""

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Add two numbers using a static method.
        
        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Multiply two numbers using a class method.
        
        This method accesses the class attribute calculation_type
        to demonstrate how class methods can interact with class-level data.
        
        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
