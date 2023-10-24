import numpy as np

def load_data():
    data = []
    with open("Texto1.txt", "r", encoding='utf-8') as datos:
        for linea in datos:
            oracion = [x for x in linea.strip().split("\n")]
            data.extend(oracion)  # Cambiar append a extend para agregar las oraciones individuales
        
    print("Se cargaron los datos")
    return data  # Unir todas las oraciones en una sola cadena

documentos = load_data()
print(documentos)
