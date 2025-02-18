from openpyxl import Workbook
libro =Workbook()
hoja = libro.active
hoja.title = "Ejemplo de datos desde py"
datos = [["NOMBRE", "EDAD", "CIUDAD"], ["Nacho", 27, "Jerecuaro"],  ["Osiel", 15, "Coroneo"],  ["Leandro", 16, "Coroneo 2"],["adolfo", 16, "Michoacan"],]
for fila in datos:
    hoja.append(fila)
nom_archivo= "datos_ejemplo.xlsx"
libro.save(nom_archivo)
print(f"Datos almacenados en el archivo {nom_archivo}")