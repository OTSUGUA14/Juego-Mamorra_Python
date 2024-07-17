class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=150, ataque=20, defensa=30, inteligencia=5, agilidad=10, fuerza=20)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=10, defensa=10, inteligencia=30, agilidad=15, fuerza=5)

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre,vida=100, ataque=15, defensa=15, inteligencia=10, agilidad=25, fuerza=10)

class Sanador(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=5, defensa=20, inteligencia=25, agilidad=10, fuerza=5)



def imprimir_atributos_tabla(personajes):
    nombres = ["ESTADISTICAS","1-GUERRERO","2-MAGO","3-ARQUERO","4-SANADOR"]
    atributos = ["vida", "ataque", "defensa", "inteligencia", "agilidad", "fuerza"]
    
    # Determinar el ancho de columna
    max_nombre_len = max(len(nombre) for nombre in nombres)
    col_width = max(max_nombre_len, 15)  # Asegurar que haya suficiente espacio para los nombres y atributos
    
    # Imprimir nombres con ancho fijo
    header = "".join(f"{nombre:<{col_width}}" for nombre in nombres)
    print(header)
    
    # Imprimir atributos con ancho fijo
    for atributo in atributos:
        linea=(f"{atributo:<{col_width}}")
        linea += " ".join(f" {getattr(personaje, atributo):<{col_width}}" for personaje in personajes)
        print(linea)

def imprimir_datos(personaje,nombre):

    atributos = ["vida", "ataque", "defensa", "inteligencia", "agilidad", "fuerza"]
    
    # Determinar el ancho de columna
    col_width = max(5, 15)  # Asegurar que haya suficiente espacio para los nombres y atributos
    
    # Imprimir nombres con ancho fijo
    header = "".join(f"{nombre:<{col_width}}")
    print("Nombre: "+ header)
    print("Clase: "+ personaje.__class__.__name__)
    
    # Imprimir atributos con ancho fijo
    for atributo in atributos:
        linea=(f"{atributo:<{col_width}}")
        linea += " ".join(f" {getattr(personaje, atributo):<{col_width}}")
        print(linea)

nombre =input("Bienvenido al juego de mamzmorra COMENZEMOS por elegir el nombre de tu personaje (Puede tener caracteres , numeros etc) :" )
# Ejemplo de creación de instancias
guerrero = Guerrero(nombre)
mago = Mago(nombre)
arquero = Arquero(nombre)
sanador = Sanador(nombre)

# Lista de personajes
personajes = [guerrero, mago, arquero, sanador]

# Imprimir atributos en formato tabular
print("-----------------------------------------------------------------------------")
imprimir_atributos_tabla(personajes)
print("-----------------------------------------------------------------------------")

while True:
    eleccion=int(input("Elegi la clase segun el nùmero que aparece(tomate tu tiempo luego no lo podras cambiar)"))
    if (eleccion==1):
        principal= Guerrero(nombre)
        break
    elif(eleccion==2):
        principal= Mago(nombre)
        break
    elif(eleccion==3):
        principal= Arquero(nombre)
        break
    elif(eleccion==4):
        principal= Sanador(nombre)
        break
    else:
        print("Eror ingrese un valor valido")

print("-----------------------------------------------------------------------------")
print("Genial tus estadistica quedan asi:")
imprimir_datos(principal,nombre)
