class Calculadora:
    def suma(self, a: float, b: float) -> float:
        """Calculates and returns the sum of a and b."""
        return a + b

    def resta(self, a: float, b: float) -> float:
        """Calculates and returns the difference of a and b."""
        return a - b

    def multiplicacion(self, a: float, b: float) -> float:
        """Calculates and returns the product of a and b."""
        return a * b

    def division(self, a: float, b: float) -> float:
        """Calculates and returns the quotient of a and b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError('No se puede dividir entre cero')
        return a / b

    def raiz_cuadrada(self, a: float) -> float:
        """Calculates and returns the square root of a. Raises ValueError if a is negative."""
        if a < 0:
            raise ValueError('No se puede calcular la raíz cuadrada de un número negativo')
        return a ** 0.5

    def potencia(self, base: float, exponente: float) -> float:
        """Calculates and returns the power of base raised to exponente."""
        return base ** exponente