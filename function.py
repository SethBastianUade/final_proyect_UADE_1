def promedio_edad(acum, lista):
    """Calcula el promedio de edad a partir de una lista de edades y el total acumulado."""
    if len(lista) == 0:  # Verificación para evitar división por cero
        return 0
    return acum / len(lista)


def ranking(lista):
    "Imprime un ranking enumerado de los elementos de una lista."

    for i in range(0, len(lista) - 1):
        print("- ", i+1, " ", lista[i])


def lista_fechas(lista, fecha_hoy):
    """Determina y muestra la fecha más lejana y la más cercana en relación con una fecha de referencia."""
    if not lista:  # Manejo de listas vacías
        print("No hay fechas en la lista.")
        return

    f_lejana = lista[0]
    f_cercana = lista[0]

    for fecha in lista:
        if fecha > f_cercana:
            f_cercana = fecha
        if fecha < f_lejana:
            f_lejana = fecha

    print(f"""
          La fecha más lejana es: {f_lejana}
          La fecha más cercana es: {f_cercana}
          """)


def lista_montos(lista):
    """Calcula y muestra el monto promedio, el máximo y el mínimo en una lista de montos."""
    if not lista:  # Manejo de listas vacías
        print("No hay montos en la lista.")
        return

    min_monto = lista[0]
    max_monto = lista[0]
    acum = 0

    for monto in lista:
        acum += monto
        if monto < min_monto:
            min_monto = monto
        if monto > max_monto:
            max_monto = monto

    prom_monto = acum / len(lista)

    print(f""" 
        El promedio del dinero declarado es: {prom_monto:.2f}
        El monto máximo declarado es: {max_monto}
        Y el mínimo es: {min_monto}
        """)


def porcentaje(lista_1, lista_2):
    """Calcula y muestra los porcentajes de dos categorías respecto al total."""
    total = len(lista_1) + len(lista_2)
    if total == 0:  # Manejo de listas vacías
        print("No hay datos para calcular porcentajes.")
        return

    porcentaje_1 = (len(lista_1) / total) * 100
    porcentaje_2 = (len(lista_2) / total) * 100

    print(f"""
          El porcentaje de bienes de Argentina es de: {porcentaje_1:.2f}%
          El porcentaje de bienes del exterior es de: {porcentaje_2:.2f}%
          """)


def bienes_stats(lista):
    """Calcula y muestra el bien más y menos declarado en una lista."""
    if not lista:  # Manejo de listas vacías
        print("No hay bienes en la lista.")
        return

    bienes_dict = {
        1: "Inmueble",
        2: "Título de Valor",
        3: "Moneda nacional/extranjera",
        4: "Criptomoneda"
    }

    # Contadores manuales para cada tipo de bien
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0
    contador_4 = 0

    for bien in lista:
        if bien == 1:
            contador_1 += 1
        elif bien == 2:
            contador_2 += 1
        elif bien == 3:
            contador_3 += 1
        elif bien == 4:
            contador_4 += 1

    lista_contadores = [contador_1, contador_2, contador_3, contador_4]

    # Encuentra el índice del máximo y mínimo manualmente
    c_max = 0
    c_min = 0
    for i in range(4):
        if lista_contadores[i] > lista_contadores[c_max]:
            c_max = i
        if lista_contadores[i] < lista_contadores[c_min]:
            c_min = i

    print(f"""
          El bien más declarado es {bienes_dict[c_max+1]} con {lista_contadores[c_max]} veces.
          Y el bien menos declarado es {bienes_dict[c_min+1]} con {lista_contadores[c_min]} veces.
          """)
