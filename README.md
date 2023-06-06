# :star: SRINGS :star:
## Un dia nuevo, un nuevo reto
REALIZANDO NUESTRO RETO #12

## PUNTOS DEL RETO
### :round_pushpin: PUNTO #1 
+  Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.
### :feet: Endswith
`sort endswith(suffix)` - Devuelve True si la cadena termina con el sufijo especificado, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "Hola, ¿cómo estás?"
print(texto.endswith("?"))  # Devuelve True
print(texto.endswith("!"))  # Devuelve False
```

### :feet: Startswith
`startswith(prefix)`- Devuelve True si la cadena comienza con el prefijo especificado, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "Hola, ¿cómo estás?"
print(texto.startswith("Hola"))  # Devuelve True
print(texto.startswith("Adiós"))  # Devuelve False
```

### :feet: Isalpha
`isalpha()` - Devuelve True si todos los caracteres de la cadena son letras (alfabéticos) y la cadena no está vacía, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "Hola"
print(texto.isalpha())  # Devuelve True

texto = "Hola123"
print(texto.isalpha())  # Devuelve False

```

### :feet: Isalnum
`isalnum()` - Devuelve True si todos los caracteres de la cadena son alfanuméricos (letras o números) y la cadena no está vacía, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "Hola123"
print(texto.isalnum())  # Devuelve True

texto = "Hola!"
print(texto.isalnum())  # Devuelve False

```

### :feet: Isdigit
`isdigit()` - Devuelve True si todos los caracteres de la cadena son dígitos numéricos y la cadena no está vacía, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "123"
print(texto.isdigit())  # Devuelve True

texto = "Hola123"
print(texto.isdigit())  # Devuelve False

```

### :feet: Isspace
`isspace()` - Devuelve True si todos los caracteres de la cadena son espacios en blanco y la cadena no está vacía, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "   "
print(texto.isspace())  # Devuelve True

texto = "Hola"
print(texto.isspace())  # Devuelve False

```

### :feet: Istitle
`istitle()` - Devuelve True si la cadena sigue una convención de título, es decir, si la primera letra de cada palabra en la cadena está en mayúscula y las demás letras están en minúscula, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "Hola, ¿Cómo Estás?"
print(texto.istitle())  # Devuelve True

texto = "Hola, ¿Cómo estás?"
print(texto.istitle())  # Devuelve False

```

### :feet:  Islower
`islower()` - Devuelve True si todos los caracteres alfabéticos de la cadena están en minúscula y la cadena no está vacía, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "hola"
print(texto.islower())  # Devuelve True

texto = "Hola"
print(texto.islower())  # Devuelve False

```

### :feet: isupper
`isupper()` - Devuelve True si todos los caracteres alfabéticos de la cadena están en mayúscula y la cadena no está vacía, de lo contrario, devuelve False.
Ejemplo:
``` ruby
texto = "HOLA"
print(texto.isupper())  # Devuelve True

texto = "Hola"
print(texto.isupper())  # Devuelve False

```


### :round_pushpin: PUNTO #2
+ Procesar el archivo y extraer: 
  + Cantidad de vocales
  + Cantidad de consonantes
  + Listado de las 50 palabras que más se repiten
  + Listado de destinatarios con cantidad de mensajes recibidos
  + Cantidad de mensajes enviados por cada día
  
#### :round_pushpin: PUNTO #2.1
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/PqR9VQvJ/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

  
#### :round_pushpin: PUNTO #2.2
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/FzBY7qYm/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


#### :round_pushpin: PUNTO #2.3
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/x1rdhLHs/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>
  
  
#### :round_pushpin: PUNTO #2.4
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/TPtfdbLv/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


#### :round_pushpin: PUNTO #2.5
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/SjbpT75C/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>
