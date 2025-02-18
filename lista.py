from os import strerror
try:
    with open ("new_file2.txt", "wt" ) as file:
            file.write("Nacho\n")
            file.write("osiel\n")
            file.write("leandro\n")
            file.write("alfrdo\n")
            file.write("alvaro\n")
    print("Archivo Escrito correctament...")

except IOError as e:
    print("se produjo un error de E/S", strerror(e.errno))
    