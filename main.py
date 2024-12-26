"""
Programa para el registro de contribuyentes al régimen de regularización de activos.
Los datos suministrados por cada contribuyente son:
- DNI, Nombre, Apellido, Edad, Fecha de nacimiento, Profesión, Fecha de declaración,
  Monto a declarar y Origen de los fondos.

Al finalizar el ingreso, el programa debe informar:
- Número de personas registradas.
- Menor y mayor edad de un registrado.
- Edad promedio de las personas registradas.
- Fecha de declaración más lejana y más cercana.
- Ranking de profesiones de las personas registradas.
- Ranking de origen de fondos de los registrados.
"""
import os
# Archivo que contiene funciones auxiliares
import function

# Listas para almacenar datos y realizar rankings
fd_lista = []
fondos_lista = []
edades_usuarios = []
ranking_prof = []
ranking_origen = []
bienes_arg = []
bienes_ext = []
bienes_gral = []

# Variables de control para estadísticas
edad_max = -1
edad_min = float('inf')
edad_acum = 0
acum_ext = 0
acum_arg = 0

# Fechas extremas
fdd_lejana = 0
fdd_cercana = 0
f_actual = 0
fdd = 0

respuesta = 0

# Fecha del dia actual
os.system('cls')
try:
    f_actual = int(input("Ingrese la fecha de hoy (aaaammdd): "))
except ValueError:
    f_actual = int(input("Fecha inválida. Ingrese 8 dígitos en formato (aaaammdd): "))
    
while len(str(f_actual)) != 8 or not str(f_actual).isdigit():
    try:
        f_actual = int(input("Fecha inválida. Ingrese 8 dígitos en formato (aaaammdd): "))
    except ValueError:
        f_actual = int(input("Fecha inválida. Ingrese 8 dígitos en formato (aaaammdd): "))
# Bucle principal de ingreso de datos
import os
while respuesta != -1:
    # Limpiar la terminal
    os.system('cls')

    # Ingreso de datos del contribuyente con validaciones
    nombre = input("Ingrese su nombre por favor: ")
    while not nombre.isalpha():
        nombre = input("Nombre inválido. Ingrese solo letras para el nombre: ")

    apellido = input("Ahora su apellido: ")
    while not apellido.isalpha():
        apellido = input("Apellido inválido. Ingrese solo letras para el apellido: ")
    
    dni = input("Ahora su DNI: ")
    while not dni.isdigit() or len(dni) != 8:
        dni = input("DNI inválido. Ingrese solo 8 dígitos numéricos para el DNI: ")

    # Edad y acumulación para cálculo de promedio
    try: 
        edad = int(input("Ahora su edad: "))
    except ValueError:
        edad = int(input("Edad inválida. Ingrese un valor positivo."))
    while edad <= 0:
        edad = int(input("Ingrese una edad válida"))
    edad_acum += edad
    edades_usuarios.append(edad)
    
    # Fecha de nacimiento y profesión
    fdn = input("Ahora su fecha de nacimiento (aaaammdd): ")
    while not fdn.isdigit() or len(fdn) != 8:
        fdn = input("Fecha de nacimiento inválida. Ingrese 8 dígitos en formato (aaaammdd): ")
    profesion = input("Ahora su profesión: ")
    while not profesion.isalpha():
        profesion = input("Profesión inválida. Ingrese solo letras para la profesión: ")
    ranking_prof.append(profesion)

    # Selección del tipo de bien
    try:
        respuesta_1 = int(input("""
            El bien a declarar es de Argentina o del exterior
            1 - Argentina
            2 - Exterior
        """))

        if respuesta_1 <= 1 or respuesta_1 >= 2:
            print("Opción inválida. Seleccione 1 o 2.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")
        respuesta_1 = int(input("""
            El bien a declarar es de Argentina o del exterior
            1 - Argentina
            2 - Exterior
        """))

    if respuesta_1 == 1:
        try:
            respuesta_2 = int(input("""
            Qué tipo de bien es:                          
                1 - Inmueble
                2 - Título de Valor
                3 - Moneda nacional/extranjera
                4 - Criptomoneda
            """))
            if respuesta_2 in [1, 2, 3, 4]:
                bienes_arg.append(respuesta_2)
                bienes_gral.append(respuesta_2)
            else:
                print("Opción inválida. Seleccione una opción del 1 al 4.")
        except ValueError:
                print("Entrada inválida. Ingrese un número.")
    elif respuesta_1 == 2:
        try:
            respuesta_2 = int(input("""
                Qué tipo de bien es:          
                1 - Inmueble
                2 - Título de Valor
                3 - Moneda extranjera
            """))
            if respuesta_2 in [1, 2, 3]:
                bienes_ext.append(respuesta_2)
                bienes_gral.append(respuesta_2)
            else:
                print("Opción inválida. Seleccione una opción del 1 al 3.")
        except ValueError:
                print("Entrada inválida. Ingrese un número.")

    # Fecha de declaración
    
    try:
        fdd = int(input("Ahora la fecha de declaración de los fondos (aaaammdd): "))
        fd_lista.append(fdd)
    except ValueError:
        print("Formato inválido. Ingrese la fecha (aaaa/mm/dd).")
    while len(str(fdd)) != 8:
        fdd = int(input("Fecha inválida. Ingrese 8 dígitos en formato (aaaammdd): "))

    

    # Monto y origen de fondos
    try:
        dinero = int(input("La cantidad de los fondos expresados en pesos: "))
    except ValueError:
        print("Monto inválido. Ingrese un número.")
    if dinero <= 0:
        print("Monto inválido. Ingrese un valor positivo.")
    else:
        fondos_lista.append(dinero)

    origen = input("Y ahora el origen de los fondos: ")
    while not origen.isalpha():
        origen = input("Origen inválido. Ingrese solo letras para el origen: ")
    ranking_origen.append(origen)

    # Actualización de mínimos y máximos
    if edad < edad_min:
        edad_min = edad
    if edad > edad_max:
        edad_max = edad

    # Verificación para terminar el ingreso
    
    try:
        respuesta = int(input("Si desea terminar, ingrese -1, de lo contrario cualquier otro número: "))
    except ValueError:
        respuesta = int(input("Entrada inválida. Ingrese un número."))

# Cálculos finales e impresión de resultados
print("La edad promedio es:", function.promedio_edad(edad_acum, edades_usuarios))
print("La edad mayor es:", edad_max)
print("La edad menor es:", edad_min)

print("Ranking de origen de fondos:")
function.ranking(ranking_origen)

print("Ranking de profesiones:")
function.ranking(ranking_prof)

# Lista de las fechas de declaracion
function.lista_fechas(fd_lista, f_actual)

# Lista de los montos declarados
function.lista_montos(fondos_lista)

# Porcentaje de bienes declarados
function.porcentaje(bienes_arg, bienes_ext)

# Declaracion de bienes
function.bienes_stats(bienes_gral)

input("Presione Enter para cerrar.")
