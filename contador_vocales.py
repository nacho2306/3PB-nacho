from os import strerror
try:
    with open("texto.txt","rt", encoding="utf-8") as archivo:
        contenido = archivo.read()
    
    contador_vocales = 0
    vocales ="aeiouAEIOU"
    for caracter in contenido:
        if caracter in vocales:
            contador_vocales += 1
    print("cantidad de vocales en el archivo: ", contador_vocales)
except IOError as error:
    print("Se produjo un error de E/S: ", strerror(error.errno))
except UnicodeDecodeError as unicode_error:
    print("Error de decodificacion de Unicode: ", unicode_error)