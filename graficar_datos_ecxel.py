from openpyxl import Workbook
import matplotlib.pyplot as plt
def ingrese_calificaciones():
    calificaciones = {}
    while True:
        nombre = input("Ingrese el nombre del alumno o fin para salir")
        if nombre.lower() == 'fin':
            break
        calificacion = float(input(f"Introduce la calificacion de {nombre}"))
        calificaciones[nombre] = calificacion
    return calificaciones
    
def guardar_en_ecxel(calificaciones):
    libro = Workbook()
    hoja= libro.active
    hoja.title="Calificaciones"
    hoja.append(["Nombre","Calificaciones" ])
    for nombre, calificacion in calificaciones.items():
        hoja.append([nombre, calificacion])
    nombre_archivo ="calificaciones.xlsx"
    libro.save(nombre_archivo)
    print(f"Calificaciones guardadas correctamente")

def graficar_calificaciones(calificaciones):
    nombres = list(calificaciones.keys())
    puntajes = list(calificaciones.values())
    plt.bar(nombres, puntajes, color ='pink')
    plt.xlabel('Estudiantes')
    plt.ylabel('Calificacions')
    plt.title('Grafico de calificaciones')
    plt.xticks(rotation=45)
    plt.ylim(0,10)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    calificaciones = ingrese_calificaciones()
    guardar_en_ecxel(calificaciones)
    graficar_calificaciones(calificaciones)