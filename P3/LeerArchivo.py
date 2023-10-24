# Leer el archivo de texto
import numpy as np

def load_data(texto):
    data = []
    with open(texto, "r", encoding='utf-8') as datos:
        oraciones = []
        for linea in datos:
            oraciones.append([x for x in linea.strip().split(".")])
            
        # Crear matriz para guardar las oraciones
        data.append(oraciones)
        
    print("Se cargaron los datos")
    return data

datos = load_data("Texto2.txt")
