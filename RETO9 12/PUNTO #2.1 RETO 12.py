def contar_vocales(texto: str):
    # Inicializamos el contador de vocales en 0
    vocales = 0

    # Iteramos sobre cada letra en el texto
    for letra in texto:
        # Verificamos si la letra está en el conjunto de vocales, tanto en minúsculas como en mayúsculas
        if letra in "aeiouAEIOU":
            # Si la letra es una vocal, incrementamos el contador de vocales en 1
            vocales += 1
    
    # Devolvemos el total de vocales encontradas en el texto
    return vocales

# Abre el archivo "mbox-short.txt" en modo lectura
with open("mbox-short.txt", 'r') as file:
    # Lee todo el contenido del archivo y lo guarda en la variable "texto"
    texto = file.read()

# Llama a la función contar_vocales con el contenido del archivo como argumento
cantidad_vocales = contar_vocales(texto)

# Imprime la cantidad de vocales en el texto
print("La cantidad de vocales en el texto es: " + str(cantidad_vocales))

# Prueba adicional de la función contar_vocales con la palabra "abecedario"
prueba = contar_vocales("abecedario")
print("La cantidad de vocales en la palabra abecedario es " + str(prueba))
