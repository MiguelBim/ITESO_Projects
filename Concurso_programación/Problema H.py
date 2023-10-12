# PROBLEMA H - SOLUCIÓN

# Definimos una lista de preposiciones, artículos y conjunciones a eliminar.
preposiciones = ["a", "ante", "bajo", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "sobre", "tras"]
articulos = ["el", "la", "los", "las", "lo", "les", "un", "uno", "una", "unos", "unas"]
conjunciones_basicas = ["y", "o", "pero", "aunque", "porque", "pues","si", "sino", "ni", "como", "mientras", "cuando", "antes", "después"]
# Inicializamos una lista vacía para almacenar los comentarios.
comentarios = []
# Inicializamos una lista vacía para almacenar los comentarios procesados.
comentarios_procesados = []
# # Inicializamos un diccionario vacío para almacenar las palabras ordenadas.
ocurrencias_palabras_ordenado = {}

# Pedimos al usuario que ingrese el número de comentarios a procesar.
C = int(input("Ingrese el número de comentarios a procesar: "))

# Validamos que el número de comentarios sea un entero positivo.
if C > 0:
    for i in range(C):
        comentario = input(f"Ingrese el comentario {i + 1} (longitud 20-80 caracteres): ").lower()
        # Validamos la longitud del comentario.
        if 20 <= len(comentario) <= 80:
            # Inicializamos una lista vacía para almacenar las palabras del comentario sin preposiciones, artículos ni conjunciones.
            palabras_filtradas = []
            # Dividimos el comentario en palabras.
            palabras = comentario.split()
            # Filtramos las palabras que no son preposiciones artículos ni conjunciones, y las unimos de nuevo.
            for palabra in palabras:
                if palabra not in preposiciones and palabra not in articulos and palabra not in conjunciones_basicas:
                    # Si cumple con el filtro, la agregamos a la lista de palabras filtradas.
                    palabras_filtradas.append(palabra)

            comentario_procesado = " ".join(palabras_filtradas)

            # Agregamos el comentario filtrado a la lista completa con todos los comentarios ya procesados.
            comentarios_procesados.append(comentario_procesado)

            # Inicializamos un diccionario para contabilizar las ocurrencias de cada palabra.
            ocurrencias_palabras = {}
            for comentario in comentarios_procesados:
                # Dividimos el comentario en palabras.
                palabras = comentario.split()
                # Contabilizamos las ocurrencias de cada palabra
                for palabra in palabras:
                    ocurrencias_palabras[palabra] = ocurrencias_palabras.get(palabra, 0) + 1
            #Ordenamos el diccionario
            ocurrencias_palabras_ordenado = dict(sorted(ocurrencias_palabras.items(), key=lambda item: item[1], reverse=True))

        else:
            print("Error → La longitud del comentario debe estar entre 20 y 80 caracteres.")

    # Guardamos las palabras en una lista ordenada por la frecuencia
    palabras_ordenadas = list(ocurrencias_palabras_ordenado.keys())

    # Se definen los porcentajes de asignación para los grupos
    porcentaje_alto = 30
    porcentaje_medio = 40
    porcentaje_bajo = 30

    # Calculamos el número de palabras por grupo
    total_palabras = len(palabras_ordenadas)
    npg_alto = round(total_palabras * (porcentaje_alto / 100))
    npg_medio = round(total_palabras * (porcentaje_medio / 100))
    npg_bajo = round(total_palabras * (porcentaje_bajo / 100))

    # Asignamos las palabras en sus grupos respectivos
    gpfa = palabras_ordenadas[:npg_alto]
    gpfm = palabras_ordenadas[npg_alto:npg_alto + npg_medio]
    gpfb = palabras_ordenadas[-npg_bajo:]

    # Transformamos las palabras de gpfa a mayúsculas
    gpfa_transformado = []
    for palabra in gpfa:
        gpfa_transformado.append(palabra.upper())

    # Transformamos las palabras de gpfm a mayúsculas y minúsculas
    gpfm_transformado = []
    for palabra in gpfm:
        palabra_transformada = ''
        for j, letra in enumerate(palabra):
            if j % 2 == 0:
                palabra_transformada += letra.upper()
            else:
                palabra_transformada += letra.lower()
        gpfm_transformado.append(palabra_transformada)

    # Transformamos las palabras de gpfb a minúsculas
    gpfb_transformado = []
    for palabra in gpfb:
        gpfb_transformado.append(palabra.lower())

    # Combinamos todas las listas en una sola
    todas_las_palabras = gpfa_transformado + gpfm_transformado + gpfb_transformado

    # Ordenamos las palabras alfabéticamente
    todas_las_palabras.sort()

    # Mostramos la nube de palabras
    length_gpfa = len(gpfa_transformado)
    length_gpfm = len(gpfm_transformado)
    i = 0
    print("\nLa nube de palabras resultante es: \n")
    for palabra in todas_las_palabras:
        print(palabra, end=" ")
        i += 1
        if i == length_gpfa or i == length_gpfa + length_gpfm:
            print()

else:
    # Iteramos para recibir los comentarios.
    print("Error → El número de comentarios debe ser un entero positivo.")