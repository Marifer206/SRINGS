def contar_consonantes(texto: str):
    # Inicializamos el contador de consonantes en 0
    consonantes = 0

    # Iteramos sobre cada letra en el texto
    for letra in texto:
        # Verificamos si la letra es un carácter alfabético y no es una vocal
        if letra.isalpha() and letra not in "aeiouAEIOU":
            # Si la letra es una consonante, incrementamos el contador de consonantes en 1
            consonantes += 1

    # Devolvemos el total de consonantes encontradas en el texto
    return consonantes

# Abre el archivo "mbox-short.txt" en modo lectura
with open("mbox-short.txt", 'r') as file:
    # Lee todo el contenido del archivo y lo guarda en la variable "texto"
    texto = file.read()

# Llama a la función contar_consonantes con el contenido del archivo como argumento
cantidad_consonantes = contar_consonantes(texto)

# Imprime la cantidad de consonantes en el texto
print("La cantidad de consonantes en el texto es: " + str(cantidad_consonantes))

# Prueba adicional de la función contar_consonantes con la palabra "abecedario"
prueba = contar_consonantes("abecedario")
print("La cantidad de consonantes en la palabra abecedario es " + str(prueba))