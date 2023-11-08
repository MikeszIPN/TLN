# Tecnologias de Lenguaje Natural
## Integrantes
* Miguel Angel Sanchez Sanjuanpa
* Navil Pineda Rugerio
* Valeria Jahzeel Castañon Hernandez

## Practica 1
Objetivo: A partir de varias oraciones con 3 palabras, realizar tokenización para encontrar raíces de palabras.
### Instrucciones
* Encontrar raíces de verbos en
  * Pasado simple con 1ra y 3ra persona del singular.
  * Infinitivo de verbos
  *  Pretérito imperfecto de todas las personas
* Encontrar raíces de palabras como sustantivo.
  *  Genero
  *  Pluralidad
  
Mencionar posición de palabra, tipo de palabra y características de esta.

## Practica 2 - Análisis de texto con one hot encoding, Embedding y bolsa de palabras.
Objetivo: El objetivo de esta práctica es realizar un análisis de texto
utilizando tres enfoques diferentes: one-hot encoding, embeddings y bolsa de
palabras (bag of words). Cada enfoque proporcionará una representación diferente
de un conjunto de oraciones de ejemplo. El objetivo es demostrar cómo estos
enfoques pueden utilizarse para representar y analizar texto en procesamiento de
lenguaje natural.
### Instrucciones
Pasos para la Práctica (Parte 1) one hot encoding

Bloque 1: Crea un diccionario de palabras con la oración dada.
Bloque 2: Crea vectores one-hot
Bloque 3: Visualiza los resultados

Pasos para la Práctica (Parte 2) embeddings

Paso 1: Instalar Gensim
Paso 2: Entrenar un modelo Word2Vec
Paso 3: Explorar embeddings
Paso 4: Realizar operaciones en el espacio semántico

Pasos para la Práctica (Parte 3) bolsa de palabras 

Paso 1: Tokenización
Paso 2: Crear un vocabulario
Paso 3: Crear la representación de bolsa de palabras
Paso 4: Visualizar los resultados

## Practica 3 - Análisis de texto con TF, IDF y TF-IDF
Objetivo: Calcular y visualizar las puntuaciones TF (Frecuencia de
Términos), IDF (Frecuencia Inversa de Documento) y TF-IDF (Frecuencia de
Términos-Inversa de Documento) para un término específico en una colección de
documentos utilizando Python.
### Instrucciones
Parte 1. Frecuencia de término 

Realiza una visualización de frecuencia de palabras dentro de una oración.

Parte 2. IDF (Frecuencia Inversa de Documento) 

Realiza la IDF de palabras presentes en las oraciones, considera que cada oración
representa un texto dif
erente. (puedes hacer algunas pruebas para probar su
funcionamiento)

Parte 3. TF-IDF (Frecuencia de Términos-Inversa de Documento) 

Realiza TF-IDF de documentos presentados en texto. Las oraciones para este código son
las oraciones presentadas en el código anterior. (Puedes hacer pruebas con otras
palabras.)

## Proyecto del 2 parcial - Resumen de textos
Objetivo: Que el alumno considere las herramientas utilizadas en el
curso sobre vectorización y análisis de texto para realizar resúmenes de bases de
datos con textos con información similar.
### Instrucciones
A partir de un corpus de 5 archivos de texto de por lo menos dos cuartillas,
considerar lo siguiente
1. Los textos deben ser considerados en archivos .txt
2. Los textos deben tener relación con respecto algún tema en específico
    * Deportes
    * Cultura
    * Política
    * Religión
    * Inteligencia artificial
    * Ciencia de datos
* De preferencia que no contengan palabras desconocidas.
3. Como primer proceso deben eliminar signos de puntuación y stopwords (es
posible realizarlo con una biblioteca)
4. Cambiar el texto a minúsculas completamente.
* Durante el proceso es posible realizar
  * Tokenización de oraciones
  * Tokenización de palabras
  * Uso de embeddings
  * TF, IDF, TF-IDF
  * Asociación entre palabras
  * Terminología
  * Relaciones semánticas
  
Mencionar posición de palabra, tipo de palabra y características de esta.
