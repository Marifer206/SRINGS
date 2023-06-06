def palabras_repetidas(texto: str):
    # Convertimos todo el texto a minúsculas
    texto = texto.lower()

    # Diccionario para almacenar el número de ocurrencias de cada palabra
    numero_de_palabras = {}

    # Reemplazamos los caracteres que no son letras ni espacios por espacios en blanco
    for s in texto:
        if not s.isalpha() and s != " ":
            texto = texto.replace(s, " ")

    # Dividimos el texto en palabras individuales
    archivo = texto.split()

    # Contamos el número de ocurrencias de cada palabra
    for l in archivo:
        # Si la palabra aún no está en el diccionario, la inicializamos en 0
        if l not in numero_de_palabras:
            numero_de_palabras[l] = 0
        # Incrementamos el contador de ocurrencias de la palabra
        numero_de_palabras[l] += 1

    # Imprimimos las palabras más repetidas (hasta las 50 más repetidas)
    for s in sorted(numero_de_palabras, reverse=True, key=lambda s: numero_de_palabras[s])[:51]:
        print("La palabra {} se repite {} veces en el texto".format(s, numero_de_palabras[s]))


with open("mbox-short.txt", 'r') as file:
    # Leemos el contenido del archivo y lo guardamos en la variable "txt"
    txt = file.read()
    # Llamamos a la función palabras_repetidas pasando el contenido del archivo como argumento
    palabras_repetidas(txt)