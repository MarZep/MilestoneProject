def generar_diccionario_peliculas ():
    peliculas_diccionario_inicial = [
        {'pelicula': "Terminator", 'director': "James Cameron", 'año': 1984},
        {'pelicula': "Rocky", 'director': "Jhon Avildsen", 'año': 1976},
        {'pelicula': "Halloween", 'director': "John Carpenter", 'año': 1978}
    ]
    return peliculas_diccionario_inicial

def agregar_pelicula (peliculas_diccionario_vfuncion):
    pelicula_a_agregar = str(input("ingrese pelicula a agregar: \n"))
    director_a_agregar = str(input("ingrese director de la pelicula a agregar: \n"))
    anio_de_pelicula_agregar = int(input("ingrese director de la pelicula a agregar: \n"))
    peliculas_diccionario_vfuncion.append({"pelicula": pelicula_a_agregar, "director": director_a_agregar, "año": anio_de_pelicula_agregar})
    return peliculas_diccionario_vfuncion

def mostrar_peliculas (peliculas_diccionario_vfuncionmostrar):
    for peliculas in peliculas_diccionario_vfuncionmostrar:
        print(f"Pelicula: {peliculas['pelicula']}    Director: {peliculas['director']}     Año: {peliculas['año']}")

#def buscar_por_titulo()
 #   str(input())


def realizar_accion (numero_accion,peliculas_diccionario_vfuncion_raccion):
    if numero_accion == 1:
        agregar_pelicula(peliculas_diccionario_vfuncion_raccion)
    elif numero_accion == 2:
        mostrar_peliculas(peliculas_diccionario_vfuncion_raccion)
    elif numero_accion == 3:
                 """funcion4"""
    else: "Salir"

### hasta aca funciones ########################################################################################

############################### MAINasd###############################

mensaje = "Seleccionar accion a realizar: 1.Agregar pelicula 2.Mostrar todas mis peliculas " \
          "3.Buscar por titulo 4.Salir \n"
accion = 0

peliculas_diccionario = generar_diccionario_peliculas()

while accion != 4:
    accion = int(input(mensaje))
    realizar_accion(accion, peliculas_diccionario)

"""for vueltas in range(2):
    try:

    except:
        buscar_por = "error"

    if buscar_por != "error" and buscar_por <=2:
        break"""


