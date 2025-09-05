class Calculadora:
    def suma(self, a: float, b: float) -> float:
        """Calcula y devuelve la suma de a y b."""
        return a + b

    def resta(self, a: float, b: float) -> float:
        """Calcula y devuelve la diferencia de a y b."""
        return a - b

    def multiplicacion(self, a: float, b: float) -> float:
        """Calcula y devuelve el producto de a y b."""
        return a * b

    def division(self, a: float, b: float) -> float:
        """Calcula y devuelve el cociente de a y b. Lanza ValueError si b es cero."""
        if b == 0:
            raise ValueError('No se puede dividir entre cero')
        return a / b  # Asegurando el uso correcto de la división en punto flotante

    def raiz_cuadrada(self, a: float) -> float:
        """Calcula y devuelve la raíz cuadrada de a. Lanza ValueError si a es negativo."""
        if a < 0:
            raise ValueError('No se puede calcular la raíz cuadrada de un número negativo')
        return a ** 0.5

    def potencia(self, base: float, exponente: float) -> float:
        """Calcula y devuelve la potencia de base elevada a exponente."""
        return base ** exponente

    def modulo(self, a: float, b: float) -> float:
        """Calcula y devuelve el módulo de a y b. Lanza ValueError si b es cero."""
        if b == 0:
            raise ValueError('No se puede calcular el módulo con un divisor de cero')
        return a % b