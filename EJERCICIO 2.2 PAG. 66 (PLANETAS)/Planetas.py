from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    """
    Clase que define objetos de tipo Planeta con sus atributos físicos y orbitales.
    """

    def __init__(
        self,
        nombre: str = None,
        cantidad_satelites: int = 0,
        masa: float = 0.0,
        volumen: float = 0.0,
        diametro: int = 0,
        distancia_sol: int = 0,
        tipo: TipoPlaneta = None,
        es_observable: bool = False,
        periodo_orbital: float = 0.0,
        periodo_rotacion: float = 0.0,
    ):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def imprimir(self):
        """
        Imprime en pantalla los datos del planeta.
        """
        tipo_str = self.tipo.value if isinstance(self.tipo, TipoPlaneta) else self.tipo
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {tipo_str}")
        print(f"Es observable = {self.es_observable}")
        print(f"Periodo orbital (años) = {self.periodo_orbital}")
        print(f"Periodo de rotación (días) = {self.periodo_rotacion}")

    def calcular_densidad(self) -> float:
        """
        Calcula y devuelve la densidad del planeta (masa / volumen).
        """
        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        """
        Determina si el planeta es exterior (> 3.4 UA).
        """
        limite = 149597870 * 3.4
        return self.distancia_sol > limite


# --- Ejecución principal ---
if __name__ == "__main__":
    p1 = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.9736e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_sol=150000000,
        tipo=TipoPlaneta.TERRESTRE,
        es_observable=True,
        periodo_orbital=1.0,
        periodo_rotacion=1.0,
    )

    p1.imprimir()
    print(f"Densidad del planeta = {p1.calcular_densidad()}")
    print(f"Es planeta exterior = {p1.es_planeta_exterior()}\n")

    p2 = Planeta(
        nombre="Júpiter",
        cantidad_satelites=79,
        masa=1.899e27,
        volumen=1.4313e15,
        diametro=139820,
        distancia_sol=750000000,
        tipo=TipoPlaneta.GASEOSO,
        es_observable=True,
        periodo_orbital=11.86,
        periodo_rotacion=0.41,
    )

    p2.imprimir()
    print(f"Densidad del planeta = {p2.calcular_densidad()}")
    print(f"Es planeta exterior = {p2.es_planeta_exterior()}")