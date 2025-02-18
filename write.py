from os import strerror
try:
    with open ("new_file.txt", "wt" ) as file:
        for i in range(10):
            s = "Linea # "+ str(i+1)+ "\n"
            file.write(s)
        print("Archivo Escrito correctament...")

except IOError as e:
    print("se produjo un error de E/S", strerror(e.errno))
    