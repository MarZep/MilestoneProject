def generar_lista_peliculas ():
    peliculas_lista_inicial = ["Terminator", "Rocky","Halloween"]
    return peliculas_lista_inicial

def agregar_pelicula (peliculas_lista_vfuncion):
    pelicula_a_agregar = str(input("ingrese pelicula a agregar: \n"))
    peliculas_lista_vfuncion.append(pelicula_a_agregar)
    return peliculas_lista_vfuncion

def mostrar_peliculas (peliculas_lista_vfuncionmostrar):
    for valor_lista_peliculas in peliculas_lista_vfuncionmostrar:
        print(valor_lista_peliculas)

#def buscar_por_titulo()
 #   str(input())


def realizar_accion (numero_accion,peliculas_lista):
    if numero_accion == 1:
        peliculas_lista = agregar_pelicula(peliculas_lista)
    elif numero_accion == 2:
        mostrar_peliculas(peliculas_lista)
    elif numero_accion == 3:
                 """funcion4"""
    else: "Salir"

### hasta aca funciones ########################################################################################

############################### MAINasd###############################

mensaje = "Seleccionar accion a realizar: 1.Agregar pelicula 2.Mostrar todas mis peliculas " \
          "3.Buscar por titulo 4.Salir \n"
accion = 0

peliculas_lista = generar_lista_peliculas()

while accion != 4:
    accion = int(input(mensaje))
    realizar_accion(accion, peliculas_lista)

"""for vueltas in range(2):
    try:

    except:
        buscar_por = "error"

    if buscar_por != "error" and buscar_por <=2:
        break"""


