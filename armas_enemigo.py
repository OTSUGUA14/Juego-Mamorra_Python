class Armas_enemigos:
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
class Arma_guerrero_enemigo_1(Armas_enemigos):
    def __init__(self):
        super().__init__(nombre="Espada del Dragón", ataque=30, agilidad=5, vida_extra=50, probabilidad_critico=15, 
                         habilidades={"Golpe de Fuego": "Inflige 50 puntos de daño adicional de fuego al enemigo y tiene una probabilidad del 10% de quemar al enemigo, causando 10 puntos de daño por turno durante 2 turnos \n"
                                      ,"Rugido del Dragón":"Aumenta la defensa en 20 puntos y la resistencia en 15 puntos durante 3 turnos\n",
                                      "Escudo en llamas":"Crea una barrera que reduce el daño recibido en un 25% durante 2 turnos\n"})

class Arma_guerrero_enemigo_2(Armas_enemigos):
    def __init__(self):
        super().__init__(nombre="Hacha de Guerra Épica", ataque=35, agilidad=3, vida_extra=40, probabilidad_critico=10, 
                         habilidades={"Golpe Terremoto": "Inflige 60 puntos de daño y aturde a todos los enemigos cercanos durante 1 turno \n "
                                      ,"Furia del Berserker":"Aumenta el ataque en 30 puntos pero reduce la defensa en 20 puntos durante 2 turnos\n",
                                      "Grito de Guerra:":"Mejora el ataque en 15 puntos y la defensa en 10 puntos de todos los aliados cercanos durante 3 turnos\n"})
Guerrero1=Arma_guerrero_ememigo_1()
Guerrero2=Arma_guerrero_ememigo_2()
Armas_guerrero=[Guerrero1,Guerrero2]

#ARMAS MAGOS
class Arma_mago1(Armas):
    def __init__(self):
        super().__init__(nombre="Bastón de Cristal Arcano", ataque=15, agilidad=10, vida_extra=20, probabilidad_critico=20, 
                         habilidades={"Rayo de Cristal:": "Inflige 50 puntos de daño adicional de fuego al enemigo y tiene una probabilidad del 10% de quemar al enemigo, causando 10 puntos de daño por turno durante 2 turnos \n"
                                      ,"Rugido del Dragón":"Aumenta la defensa en 20 puntos y la resistencia en 15 puntos durante 3 turnos\n",
                                      "Escudo en llamas":"Crea una barrera que reduce el daño recibido en un 25% durante 2 turnos\n"})




def mostrar_armas(armas):
    nombres = ["ESTADISTICAS",armas[0].nombre,armas[1].nombre]
    atributos = ["ataque", "agilidad", "vida_extra", "probabilidad_critico"]
    
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