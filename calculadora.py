class Calculadora:
    def suma(self, a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b

    def resta(self, a: float, b: float) -> float:
        """Returns the difference of a and b."""
        return a - b

    def multiplicacion(self, a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b

    def division(self, a: float, b: float) -> float:
        """Returns the quotient of a and b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError('No se puede dividir entre cero')
        return a / b