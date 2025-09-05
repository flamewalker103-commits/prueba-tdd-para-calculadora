class Calculadora:
    def suma(self, a, b):
        """Returns the sum of a and b."""
        return a + b

    def resta(self, a, b):
        """Returns the difference of a and b."""
        return a - b

    def multiplicacion(self, a, b):
        """Returns the product of a and b."""
        return a * b

    def division(self, a, b):
        """Returns the quotient of a and b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError('No se puede dividir entre cero')
        return a / b