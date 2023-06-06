def contar_mensajes_diarios(texto: str):
    mensaje = []  # Lista para almacenar los segmentos de mensajes
    palabras = texto.split()  # Dividimos el texto en palabras

    for i in range(len(palabras)):
        if palabras[i] == "Received:":  # Verificamos si encontramos la palabra "Received:"
            segmento = []
            while palabras[i] != "-0500" and palabras[i] != "(GMT)":  # Iteramos hasta encontrar el final del segmento
                segmento.append(palabras[i])  # Añadimos cada palabra al segmento
                i += 1
            mensaje.append(segmento)  # Añadimos el segmento a la lista de mensajes

    m_dia = {}  # Diccionario para almacenar el número de mensajes por día

    for segmento in mensaje:
        indice = segmento.index('Jan')  # Obtenemos el índice de la palabra 'Jan'
        dia = int(segmento[indice - 1])  # Obtenemos el día anterior a 'Jan' y lo convertimos a entero
        if dia in m_dia:
            m_dia[dia] += 1  # Si el día ya existe en el diccionario, incrementamos su contador
        else:
            m_dia[dia] = 1  # Si el día no existe en el diccionario, lo inicializamos en 1

    return m_dia


with open("mbox-short.txt", "r") as file:
    # Abrimos el archivo "programacion.txt" en modo lectura
    # y leemos su contenido en la variable "texto"

    m_dia = contar_mensajes_diarios(file.read())
    # Llamamos a la función contar_mensajes_diarios pasando el contenido del archivo como argumento
    # y guardamos el resultado en la variable "m_dia"

    for dia in m_dia:
        print(f"Se enviaron {m_dia[dia]} mensajes el {dia} de enero, 2008")
        # Imprimimos el número de mensajes enviados para cada día en un formato legible