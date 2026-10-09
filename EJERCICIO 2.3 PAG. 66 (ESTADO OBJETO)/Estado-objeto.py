from enum import Enum

# --- Definición de Enumeraciones ---
class TipoCombustible(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"

class TipoAutomovil(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"

# --- Clase Automovil ---
class Automovil:
    """
    Clase que define objetos de tipo Automóvil con sus especificaciones,
    métodos de control de velocidad y gestión de multas.
    """

    def __init__(
        self,
        marca: str,
        modelo: int,
        motor: int,
        tipo_combustible: TipoCombustible,
        tipo_automovil: TipoAutomovil,
        numero_puertas: int,
        cantidad_asientos: int,
        velocidad_maxima: int,
        color: TipoColor,
        es_automatico: bool = False,
        valor_multa_unitaria: float = 100.0,
    ):
        """
        Constructor de la clase Automovil.
        """
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color
        self._velocidad_actual = 0
        self._es_automatico = es_automatico
        self._cantidad_multas = 0
        self._valor_multa_unitaria = valor_multa_unitaria

    # --- Métodos Getters ---
    def get_marca(self) -> str:
        return self._marca

    def get_modelo(self) -> int:
        return self._modelo

    def get_motor(self) -> int:
        return self._motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self._tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self._tipo_automovil

    def get_numero_puertas(self) -> int:
        return self._numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self._cantidad_asientos

    def get_velocidad_maxima(self) -> int:
        return self._velocidad_maxima

    def get_color(self) -> TipoColor:
        return self._color

    def get_velocidad_actual(self) -> int:
        return self._velocidad_actual

    def get_es_automatico(self) -> bool:
        return self._es_automatico

    # --- Métodos Setters ---
    def set_marca(self, marca: str):
        self._marca = marca

    def set_modelo(self, modelo: int):
        self._modelo = modelo

    def set_motor(self, motor: int):
        self._motor = motor

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible):
        self._tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil):
        self._tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas: int):
        self._numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos: int):
        self._cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima: int):
        self._velocidad_maxima = velocidad_maxima

    def set_color(self, color: TipoColor):
        self._color = color

    def set_velocidad_actual(self, velocidad_actual: int):
        self._velocidad_actual = velocidad_actual

    def set_es_automatico(self, es_automatico: bool):
        self._es_automatico = es_automatico

    # --- Métodos de Comportamiento / Negocio ---
    def acelerar(self, incremento_velocidad: int):
        """
        Incrementa la velocidad. Si intenta superar la velocidad máxima,
        genera e incrementa una multa.
        """
        if self._velocidad_actual + incremento_velocidad <= self._velocidad_maxima:
            self._velocidad_actual += incremento_velocidad
        else:
            self._cantidad_multas += 1
            print(
                f"¡Multa generada! Intento de superar la velocidad máxima "
                f"({self._velocidad_maxima} km/h). Multas acumuladas: {self._cantidad_multas}"
            )

    def desacelerar(self, decremento_velocidad: int):
        """
        Disminuye la velocidad sin permitir valores negativos.
        """
        if self._velocidad_actual - decremento_velocidad >= 0:
            self._velocidad_actual -= decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        """
        Coloca la velocidad actual en cero.
        """
        self._velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: float) -> float:
        """
        Calcula el tiempo estimado de llegada en horas (distancia / velocidad actual).
        """
        if self._velocidad_actual == 0:
            print("El automóvil está detenido. No se puede calcular el tiempo.")
            return float("inf")
        return distancia / self._velocidad_actual

    def tiene_multas(self) -> bool:
        """
        Devuelve True si el vehículo registra al menos una multa.
        """
        return self._cantidad_multas > 0

    def obtener_valor_total_multas(self) -> float:
        """
        Devuelve el valor total a pagar por multas acumuladas.
        """
        return self._cantidad_multas * self._valor_multa_unitaria

    def imprimir(self):
        """
        Muestra en pantalla todos los atributos del automóvil.
        """
        tipo_comb_str = (
            self._tipo_combustible.value
            if isinstance(self._tipo_combustible, TipoCombustible)
            else self._tipo_combustible
        )
        tipo_auto_str = (
            self._tipo_automovil.value
            if isinstance(self._tipo_automovil, TipoAutomovil)
            else self._tipo_automovil
        )
        color_str = (
            self._color.value if isinstance(self._color, TipoColor) else self._color
        )

        print(f"Marca = {self._marca}")
        print(f"Modelo = {self._modelo}")
        print(f"Motor = {self._motor}")
        print(f"Tipo de combustible = {tipo_comb_str}")
        print(f"Tipo de automóvil = {tipo_auto_str}")
        print(f"Número de puertas = {self._numero_puertas}")
        print(f"Cantidad de asientos = {self._cantidad_asientos}")
        print(f"Velocidad máxima = {self._velocidad_maxima}")
        print(f"Color = {color_str}")
        print(f"Velocidad actual = {self._velocidad_actual}")
        print(f"Es automático = {self._es_automatico}")
        print(f"Tiene multas = {self.tiene_multas()}")
        print(f"Total valor multas = ${self.obtener_valor_total_multas():.2f}")


# --- Bloque principal de prueba ---
if __name__ == "__main__":
    # Creación del automóvil
    auto1 = Automovil(
        marca="Ford",
        modelo=2018,
        motor=3,
        tipo_combustible=TipoCombustible.DIESEL,
        tipo_automovil=TipoAutomovil.EJECUTIVO,
        numero_puertas=5,
        cantidad_asientos=6,
        velocidad_maxima=250,
        color=TipoColor.NEGRO,
        es_automatico=True,
    )

    print("--- Datos iniciales del Automóvil ---")
    auto1.imprimir()

    print("\n--- Pruebas de movimiento y multas ---")
    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")

    auto1.acelerar(20)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")

    # Intento de aceleración que supera la velocidad máxima (120 + 150 = 270 > 250)
    auto1.acelerar(150)

    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")

    auto1.frenar()
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")

    auto1.desacelerar(20)

    print(f"\n¿Tiene multas el vehículo?: {auto1.tiene_multas()}")
    print(f"Monto total de multas: ${auto1.obtener_valor_total_multas():.2f}")