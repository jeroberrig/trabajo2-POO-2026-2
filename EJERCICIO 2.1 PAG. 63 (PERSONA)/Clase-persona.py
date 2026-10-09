class Persona:
    def __init__(self, nombre: str, apellidos: str, numero_documento_identidad: str, ano_nacimiento: int, pais_nacimiento: str, genero: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.ano_nacimiento = ano_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero

    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.numero_documento_identidad}")
        print(f"Año de nacimiento = {self.ano_nacimiento}")
        print(f"País de nacimiento = {self.pais_nacimiento}")
        print(f"Género = {self.genero}")
        print()

if __name__ == "__main__":
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998, "Colombia", "H")
    p2 = Persona("Luis", "León", "1053223344", 2001, "México", "H")

    p1.imprimir()
    p2.imprimir()