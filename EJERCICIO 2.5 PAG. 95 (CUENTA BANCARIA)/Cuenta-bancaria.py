from enum import Enum


# --- Enumeración para el tipo de cuenta ---
class TipoCuenta(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"


# --- Clase CuentaBancaria ---
class CuentaBancaria:
    """Clase que define objetos que representan una cuenta bancaria con datos del titular,

    saldo, tipo de cuenta y porcentaje de interés mensual.
    """

    def __init__(
        self,
        nombres_titular: str,
        apellidos_titular: str,
        numero_cuenta: int,
        tipo_cuenta: TipoCuenta,
        porcentaje_interes_mensual: float = 0.0,
    ):
        """Constructor de la clase CuentaBancaria.

        Inicializa el saldo en cero por defecto.
        """
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0
        self.porcentaje_interes_mensual = porcentaje_interes_mensual

    def imprimir(self):
        """Imprime en pantalla los datos de la cuenta bancaria."""
        tipo_str = (
            self.tipo_cuenta.value
            if isinstance(self.tipo_cuenta, TipoCuenta)
            else self.tipo_cuenta
        )
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {tipo_str}")
        print(f"Saldo = ${self.saldo:.2f}")
        print(
            f"Porcentaje de interés mensual = {self.porcentaje_interes_mensual}%"
        )

    def consultar_saldo(self):
        """Imprime en pantalla el saldo actual de la cuenta bancaria."""
        print(f"El saldo actual es = ${self.saldo:.2f}")

    def consignar(self, valor: float) -> bool:
        """Actualiza y devuelve el saldo a partir de un valor a consignar (> 0)."""
        if valor > 0:
            self.saldo += valor
            print(
                f"Se ha consignado ${valor:.2f} en la cuenta. El nuevo saldo es ${self.saldo:.2f}"
            )
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor: float) -> bool:
        """Actualiza y devuelve el saldo a partir de un valor a retirar (> 0 y <= saldo)."""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(
                f"Se ha retirado ${valor:.2f} en la cuenta. El nuevo saldo es ${self.saldo:.2f}"
            )
            return True
        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False

    def aplicar_interes_mensual(self) -> float:
        """Calcula el nuevo saldo aplicando el porcentaje de interés mensual correspondiente."""
        interes_generado = self.saldo * (
            self.porcentaje_interes_mensual / 100.0
        )
        self.saldo += interes_generado
        print(
            f"Se ha aplicado un interés del {self.porcentaje_interes_mensual}%. "
            f"Interés generado = ${interes_generado:.2f}. El nuevo saldo es ${self.saldo:.2f}"
        )
        return self.saldo


# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    # Creación de la cuenta con un interés mensual del 1.5%
    cuenta = CuentaBancaria(
        "Pedro",
        "Pérez",
        123456789,
        TipoCuenta.AHORROS,
        porcentaje_interes_mensual=1.5,
    )

    print("--- Datos Iniciales de la Cuenta ---")
    cuenta.imprimir()

    print("\n--- Operaciones de Transacción ---")
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)

    print("\n--- Aplicación de Tasa de Interés ---")
    cuenta.aplicar_interes_mensual()