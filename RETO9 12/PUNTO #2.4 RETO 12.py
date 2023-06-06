def destino(texto: str):
    # Dividimos el texto en palabras
    palabras = texto.split()

    # Diccionario para almacenar el número de ocurrencias de cada destinatario
    destinatario = {}

    for i in range(1, len(palabras)):
        # Verificamos si la palabra actual es "by" o "BY" y si la palabra anterior contiene un punto (indicando un posible destinatario)
        if (palabras[i] == "by" or palabras[i] == "BY") and "." in palabras[i-1]:
            if palabras[i+1] in destinatario:
                # Si el destinatario ya existe en el diccionario, incrementamos su contador en 1
                destinatario[palabras[i+1]] += 1
            else:
                # Si el destinatario no existe en el diccionario, lo agregamos con un contador inicial de 1
                destinatario[palabras[i+1]] = 1

    # Convertimos el diccionario a una lista de tuplas (destinatario, contador)
    listado = list(destinatario.items())

    return listado

with open("mbox-short.txt", "r") as file:
    # Leemos el contenido del archivo y llamamos a la función destino pasando el texto como argumento
    nombres = destino(file.read())
    for nombre, contador in nombres:
        # Imprimimos cada destinatario y su contador en un formato agradable
        print("El destinatario {} aparece {} veces en el texto".format(nombre, contador))