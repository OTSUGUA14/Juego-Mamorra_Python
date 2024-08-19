class Armas:
    def __init__(self, nombre, ataque, agilidad, vida_extra, probabilidad_critico, habilidades=None):
        self.nombre=nombre
        self.ataque=ataque
        self.agilidad=agilidad
        self.vida_extra=vida_extra
        
        self.probabilidad_critico=probabilidad_critico
        if habilidades is None:
            habilidades={}
        self.habilidades=habilidades
    
# ARMAS GUERRO
class Arma_guerre1(Armas):
    def __init__(self):
        super().__init__(nombre="Espada del Dragón", ataque=30, agilidad=5, vida_extra=50, probabilidad_critico=15,
                         habilidades={"Corte Feroz":"25 puntos de daño físico.\n"
                                      ,"Golpe de Fuego": " (Costo de mana: 20) Inflige 50 puntos de daño adicional de fuego al enemigo y tiene una probabilidad del 10% de quemar al enemigo, causando 10 puntos de daño por turno durante 2 turnos \n"
                                      ,"Rugido del Dragón":" (Costo de mana: 15) Aumenta la defensa en 20 puntos y la resistencia en 15 puntos durante 3 turnos\n",
                                      "Escudo en llamas":"(Costo de mana: 25) Crea una barrera que reduce el daño recibido en un 25% durante 2 turnos\n"})

class Arma_guerre2(Armas):
    def __init__(self):
        super().__init__(nombre="Hacha de Guerra Épica", ataque=35, agilidad=3, vida_extra=40, probabilidad_critico=10,
                         habilidades={"Hachazo Devastador":"30 puntos de daño físico.\n",
                             "Golpe Terremoto": " (Costo de mana: 30) Inflige 60 puntos de daño y aturde a todos los enemigos cercanos durante 1 turno \n "
                                      ,"Furia del Berserker":"(Costo de mana: 25) Aumenta el ataque en 30 puntos pero reduce la defensa en 20 puntos durante 2 turnos\n",
                                      "Grito de Guerra:":"(Costo de mana: 25) Mejora el ataque en 15 puntos y la defensa en 10 puntos de todos los aliados cercanos durante 3 turnos\n"})
Guerrero1=Arma_guerre1()
Guerrero2=Arma_guerre2()
Armas_guerrero=[Guerrero1,Guerrero2]

#ARMAS MAGOS
class Arma_mago1(Armas):
    def __init__(self):
        super().__init__(nombre="Bastón de Cristal Arcano", ataque=15, agilidad=10, vida_extra=20, probabilidad_critico=20,
                         habilidades={" Descarga Mágica":" 20 puntos de daño mágico.\n",
                             "Rayo de Cristal:": "(Costo de mana: 30) Inflige 40 puntos de daño mágico y tiene una probabilidad de crítico del 50%.\n"
                                      ,"Escudo Arcano:":"(Costo de mana: 20) Absorbe hasta 60 puntos de daño durante 2 turnos.\n",
                                      "Curación Arcana":"(Costo de mana: 25) Restaura 30 puntos de vida a todos los aliados cercanos.\n"})

class Arma_mago2(Armas):
    def __init__(self):
        super().__init__(nombre="Vara del Sabio", ataque=10, agilidad=8, vida_extra=25, probabilidad_critico=25, 
                         habilidades={"Rayo de Luz":"15 puntos de daño mágico.\n",
                             "Tormenta Mágica:": "(Costo de mana: 40) Inflige 50 puntos de daño a todos los enemigos en un área determinada.\n"
                                      ,"Teletransportación:":" (Costo de mana: 20):  Permite al mago moverse instantáneamente a cualquier lugar del campo de batalla.\n",
                                      "Amplificación de Hechizos:":" (Costo de mana: 25): Aumenta el poder de los hechizos en un 30% durante 3 turnos.\n"})
Mago1=Arma_mago1()
Mago2=Arma_mago2()
Armas_mago=[Mago1,Mago2]

#ARMAS ARQUERO
class Arma_arque1(Armas):
    def __init__(self):
        super().__init__(nombre="Arco del Halcón", ataque=25, agilidad=15, vida_extra=30, probabilidad_critico=20,
                         habilidades={"Flecha Precisa":" 20 puntos de daño físico.\n",
                             "Flecha Rápida:": " (Costo de mana: 15)  Inflige 35 puntos de daño y tiene una probabilidad de crítico del 40%.\n"
                                      ,"Ojo de Águila:":" (Costo de mana: 20) Aumenta la precisión y el alcance en un 25% durante 3 turnos.\n",
                                      "Flecha Explosiva":" (Costo de mana: 25) Inflige 30 puntos de daño al objetivo principal y 20 puntos de daño a los enemigos cercanos.\n"})

class Arma_arque2(Armas):
    def __init__(self):
        super().__init__(nombre="Ballesta de la Sombra", ataque=20, agilidad=20, vida_extra=25, probabilidad_critico=25, mana=150,
                         habilidades={" Disparo Silencioso":"18 puntos de daño físico.\n",
                             "Flecha de Sombra:": "  Inflige 40 puntos de daño y atraviesa obstáculos.\n"
                                      ,"Paso Sombrío:":" Permite al arquero moverse furtivamente por el campo de batalla sin ser detectado durante 2 turnos.\n",
                                      "Disparo Triple:":" Lanza tres flechas, cada una inflige 25 puntos de daño a diferentes objetivos.\n"})

Arquero1=Arma_arque1()
Arquero2=Arma_arque2()
Armas_arque=[Arquero1,Arquero2]

#ARMAS SANADOR

class Arma_sana1(Armas):
    def __init__(self):
        super().__init__(nombre=" Cetro de la Vida", ataque=10, agilidad=5, vida_extra=40, probabilidad_critico=10, 
                         habilidades={"Sanación Masiva:": "Restaura 50 puntos de vida a todos los aliados cercanos.\n"
                                      ,"Escudo de Luz:":" Crea un escudo que reduce el daño recibido en un 20% durante 2 turnos.\n",
                                      "Rejuvenecimiento:":"  Regenera 15 puntos de vida por turno a un aliado durante 3 turnos.\n"})

class Arma_sana2(Armas):
    def __init__(self):
        super().__init__(nombre="  Bastón del Guardián", ataque=5, agilidad=8, vida_extra=35, probabilidad_critico=15, 
                         habilidades={"SCuración Rápida:": " Restaura instantáneamente 40 puntos de vida a un aliado.\n"
                                      ,"Protección Divina":" Aumenta la defensa en 20 puntos de un aliado durante 3 turnos.\n",
                                      "Purificación:":" Elimina todos los efectos negativos de un aliado y restaura 10 puntos de vida.\n"})

Sanador1=Arma_sana1()
Sanador2=Arma_sana2()
Armas_sana=[Sanador1,Sanador2]

def mostrar_armas(armas):
    nombres = ["ESTADISTICAS",armas[0].nombre,armas[1].nombre]
    atributos = ["ataque", "agilidad", "vida_extra", "probabilidad_critico","mana"]
    
    # Determinar el ancho de columna
    max_nombre_len = max(len(nombre) for nombre in nombres)
    col_width = max(max_nombre_len, 25)  # Asegurar que haya suficiente espacio para los nombres y atributos
    
    # Imprimir nombres con ancho fijo
    header = "".join(f"{nombre:<{col_width}}" for nombre in nombres)
    print(header)
    
    for atributo in atributos:
        linea = f"{atributo:<{col_width}}"
        linea += " ".join(f"{str(getattr(arma, atributo)):<{col_width}}" for arma in armas)
        print(linea)
    
    # Imprimir habilidades con un formato separado
    print("\nHABILIDADES:")
    print("----------------------------------------------------")
    for arma in armas:
        habilidades = getattr(arma, "habilidades")
        print(f"\n{arma.nombre}:")
        for nombre, descripcion in habilidades.items():
            print(f"{nombre}: {descripcion}")
        print("----------------------------------------------------")