from os import strerror
try:
    with open("texto.txt","rt", encoding="utf-8") as archivo:
        contenido = archivo.read()
    
    contador_vocales = 0
    contador_consonantes = 0
    contador_espacios = 0
    vocales ="aeiouAEIOU"
    consonates = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    espacios = " "
    for caracter in contenido:
        if caracter in vocales:
            contador_vocales += 1
        elif caracter in consonates:
            contador_consonantes += 1
        elif caracter in espacios:
            contador_espacios += 1

    print("cantidad de vocales en el archivo: ", contador_vocales)
    print("cantidad de consonantes en el archivo: ", contador_consonantes)
    print("cantidad de espacios en el archivo: ", contador_espacios)
except IOError as error:
    print("Se produjo un error de E/S: ", strerror(error.errno))
except UnicodeDecodeError as unicode_error:
    print("Error de decodificacion de Unicode: ", unicode_error)