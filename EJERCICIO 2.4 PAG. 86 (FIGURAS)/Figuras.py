import math

class Circulo:
    """Clase que define un círculo a partir de su radio."""

    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo: π * r²."""
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del círculo: 2 * π * r."""
        return 2 * math.pi * self.radio


class Rectangulo:
    """Clase que define un rectángulo a partir de su base y altura."""

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo: base * altura."""
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del rectángulo: (2 * base) + (2 * altura)."""
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:
    """Clase que define un cuadrado a partir de la longitud de su lado."""

    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado: lado²."""
        return self.lado * self.lado

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del cuadrado: 4 * lado."""
        return 4 * self.lado


class TrianguloRectangulo:
    """Clase que define un triángulo rectángulo a partir de su base y altura."""

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del triángulo rectángulo: (base * altura) / 2."""
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        """Calcula la hipotenusa utilizando el teorema de Pitágoras."""
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro: suma de base, altura e hipotenusa."""
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        """Determina el tipo de triángulo (Equilátero, Escaleno o Isósceles)."""
        hipotenusa = self.calcular_hipotenusa()

        if self.base == self.altura == hipotenusa:
            print("Es un triángulo equilátero")
        elif (
            self.base != self.altura
            and self.base != hipotenusa
            and self.altura != hipotenusa
        ):
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


# --- Ejercicios Propuestos ---


class Rombo:
    """Clase que define un rombo a partir de sus diagonales y su lado."""

    def __init__(
        self, diagonal_mayor: float, diagonal_menor: float, lado: float
    ):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del rombo: (Diagonal Mayor * Diagonal Menor) / 2."""
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del rombo: 4 * lado."""
        return 4 * self.lado


class Trapecio:
    """
    Clase que define un trapecio a partir de sus bases, altura y lados no paralelos.
    """

    def __init__(
        self,
        base_mayor: float,
        base_menor: float,
        altura: float,
        lado1: float,
        lado2: float,
    ):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self) -> float:
        """Calcula el área del trapecio: ((Base Mayor + Base Menor) * altura) / 2."""
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del trapecio: Base Mayor + Base Menor + Lado1 + Lado2."""
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2


# --- Prueba de Figuras ---
if __name__ == "__main__":
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)

    # Nuevas figuras
    figura5 = Rombo(diagonal_mayor=8, diagonal_menor=6, lado=5)
    figura6 = Trapecio(
        base_mayor=10, base_menor=6, altura=4, lado1=5, lado2=5
    )

    print(f"El área del círculo es = {figura1.calcular_area():.2f}")
    print(f"El perímetro del círculo es = {figura1.calcular_perimetro():.2f}\n")

    print(f"El área del rectángulo es = {figura2.calcular_area()}")
    print(
        f"El perímetro del rectángulo es = {figura2.calcular_perimetro()}\n"
    )

    print(f"El área del cuadrado es = {figura3.calcular_area()}")
    print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro()}\n")

    print(f"El área del triángulo es = {figura4.calcular_area()}")
    print(
        f"El perímetro del triángulo es = {figura4.calcular_perimetro():.2f}"
    )
    figura4.determinar_tipo_triangulo()
    print()

    # Pruebas de las nuevas figuras requeridas
    print("--- Ejercicios Propuestos ---")
    print(f"El área del rombo es = {figura5.calcular_area()}")
    print(f"El perímetro del rombo es = {figura5.calcular_perimetro()}\n")

    print(f"El área del trapecio es = {figura6.calcular_area()}")
    print(f"El perímetro del trapecio es = {figura6.calcular_perimetro()}")