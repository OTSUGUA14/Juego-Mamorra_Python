class Enemigo:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza

#Enemigo Guardian 
class guardian_enemigo_fuego(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=120, ataque=18, defensa=25, inteligencia=5, agilidad=8, fuerza=18,)

class guardian_enemigo_hielo(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=120, ataque=18, defensa=25, inteligencia=5, agilidad=8, fuerza=18,)

class guardian_enemigo_sombra(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=120, ataque=18, defensa=25, inteligencia=5, agilidad=8, fuerza=18,)


#Enemigo Hechicero
class hechicero_enemigo_veneno(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, ataque=12, defensa=8, inteligencia=28, agilidad=12, fuerza=4)

class hechicero_enemigo_rayo(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, ataque=12, defensa=8, inteligencia=28, agilidad=12, fuerza=4)

class hechicero_enemigo_oscuridad(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, ataque=12, defensa=8, inteligencia=28, agilidad=12, fuerza=4)


#Enemigo Arquero
class arquero_enemigo_cristal(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=13, defensa=12, inteligencia=8, agilidad=22, fuerza=8)

class arquero_enemigo_veneno(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=13, defensa=12, inteligencia=8, agilidad=22, fuerza=8)

class arquero_enemigo_fuego(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=13, defensa=12, inteligencia=8, agilidad=22, fuerza=8)

#Enemigo Sanador
class druida_enemigo_naturaleza(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=4, defensa=18, inteligencia=23, agilidad=9, fuerza=4)

class druida_enemigo_espiritual(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=4, defensa=18, inteligencia=23, agilidad=9, fuerza=4)

class druida_enemigo_sabio(Enemigo):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=4, defensa=18, inteligencia=23, agilidad=9, fuerza=4)



