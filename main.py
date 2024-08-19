import personaje
import armas

nombre =input("Bienvenido al juego de mazmorra COMENCEMOS por elegir el nombre de tu personaje (Puede tener caracteres , numeros etc) : " )
print("-----------------------------------------------------------------------------")
guerrero = personaje.Guerrero(nombre)
mago = personaje.Mago(nombre)
arquero = personaje.Arquero(nombre)
sanador = personaje.Sanador(nombre)
personajes = [guerrero, mago, arquero, sanador]
personaje.imprimir_atributos_tabla(personajes)

print("-----------------------------------------------------------------------------")
while True:
    eleccion=int(input("Elegi la clase segun el nùmero que aparece(tomate tu tiempo luego no lo podras cambiar): "))
    if (eleccion==1):
        principal= personaje.Guerrero(nombre)
        break
    elif(eleccion==2):
        principal= personaje.Mago(nombre)
        break
    elif(eleccion==3):
        principal= personaje.Arquero(nombre)
        break
    elif(eleccion==4):
        principal= personaje.Sanador(nombre)
        break
    else:
        print("Eror ingrese un valor valido")

print("-----------------------------------------------------------------------------")
print("Genial Ahora a elegir tu arma inicial:")
arma=armas.Armas_guerrero

armas.mostrar_armas(arma)
# personaje.imprimir_datos(principal,nombre)

