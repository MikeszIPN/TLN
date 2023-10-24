# Leer el archivo de texto
import numpy as np

def load_data():
    data = []
    with open("Texto1.txt", "r", encoding='utf-8') as datos:
        oraciones = []
        for linea in datos:
            oraciones.append([x for x in linea.strip().split(".")])
            
        # Crear matriz para guardar las oraciones
        data.append(oraciones)
        
    print("Se cargaron los datos")
    return data