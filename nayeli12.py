print("¡Nivel completado!")

class Personaje:

    def __init__(self, nombre, vida, arma, planeta):
        self.nombre = nombre
        self.vida = vida
        self.arma = arma
        self.planeta = planeta

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Vida:", self.vida)
        print("Arma:", self.arma)
        print("Planeta:", self.planeta)

    def atacar(self):
        print(self.nombre, "está atacando")


class Jugador(Personaje):

    def __init__(self, nombre, vida, arma, planeta, nivel, dinero):
        super().__init__(nombre, vida, arma, planeta)
        self.nivel = nivel
        self.dinero = dinero

    def informacion(self):
        self.mostrar()
        print("Nivel:", self.nivel)
        print("Dinero:", self.dinero)

    def ganar_experiencia(self):
        print("Ganaste experiencia y puedes subir de nivel")


print("ROGUE GALAXY")

jugador = Jugador(
    input("Nombre del jugador: "),
    100,
    "Espada láser",
    "Planeta desconocido",
    1,
    500
)

jugador.informacion()
jugador.atacar()
jugador.ganar_experiencia()