def generar_diccionario_peliculas():
    peliculas_diccionario_inicial = [
        {'pelicula': "Terminator", 'director': "James Cameron", 'año': 1984},
        {'pelicula': "Rocky", 'director': "Jhon Avildsen", 'año': 1976},
        {'pelicula': "Halloween", 'director': "John Carpenter", 'año': 1978}
    ]
    return peliculas_diccionario_inicial


def agregar_pelicula(peliculas_diccionario_vfuncion):
    pelicula_a_agregar = str(input("ingrese pelicula a agregar: \n"))
    director_a_agregar = str(input("ingrese director de la pelicula a agregar: \n"))
    anio_de_pelicula_agregar = int(input("ingrese director de la pelicula a agregar: \n"))
    peliculas_diccionario_vfuncion.append({"pelicula": pelicula_a_agregar, "director": director_a_agregar,
                                           "año": anio_de_pelicula_agregar})
    return peliculas_diccionario_vfuncion


def mostrar_peliculas(peliculas_diccionario_vfuncionmostrar):
    for peliculas in peliculas_diccionario_vfuncionmostrar:
        print(f"Pelicula: {peliculas['pelicula']}    Director: {peliculas['director']}     Año: {peliculas['año']}")

    print("\n")


def mostrar_peliculas_por_titulo(peliculas_diccionario_vfuncionmostrar):
    encontrada = 0
    titulo_a_buscar = str(input("Ingrese nombre de titulo a buscar \n"))

    for peliculas in peliculas_diccionario_vfuncionmostrar:
        if encontrada == 0:
            if titulo_a_buscar == peliculas['pelicula']:
                encontrada = 1
                print(f"Pelicula: {peliculas['pelicula']}    Director: {peliculas['director']}"
                      f"     Año: {peliculas['año']} \n")
            else:
                encontrada = 0

    if encontrada == 0:
        print("No se encontró la pelicula \n")


def realizar_accion(numero_accion, peliculas_diccionario_vfuncion_raccion):
    opcion_de_usuario = {
        "1": agregar_pelicula,
        "2": mostrar_peliculas,
        "3": mostrar_peliculas_por_titulo
    }

    if str(numero_accion) in opcion_de_usuario:
        funcion_elegida = opcion_de_usuario[str(numero_accion)]
        funcion_elegida(peliculas_diccionario_vfuncion_raccion)
    elif int(numero_accion) > 4:
        print("Número equivocado, seleccione dentro de 1-4 \n")


#  hasta aca funciones

#  MAIN


mensaje = "Seleccionar accion a realizar: 1.Agregar pelicula 2.Mostrar todas mis peliculas " \
          "3.Buscar por titulo 4.Salir \n"
accion = 0


peliculas_diccionario = generar_diccionario_peliculas()

while accion != 4:
    accion = int(input(mensaje))
    realizar_accion(accion, peliculas_diccionario)
