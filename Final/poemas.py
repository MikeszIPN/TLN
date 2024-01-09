from pylabeador import syllabify

def tipo_acentuacion(palabras_finales, silabas):
     vocales = ['a', 'e', 'i', 'o', 'u']
     vocal_acento = ['á', 'é', 'í', 'ó', 'ú']
     consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
     monosilabas = []
     agudas = []
     graves = []
     esdrujulas = []
     clasificador = []


     flagA = False
     flagG = False
   
     for silaba in silabas:
           # para las monosilabas
          # tienen 1, 2 o 3 letras
          if len(silaba) == 1:
               clasificador.append("monosilaba")
               monosilabas.append(silaba)
               silabas.remove(silaba)
               continue
          # agudas - acento en la ultima silaba
          if silaba[-1] in vocal_acento:
               clasificador.append("aguda")
               agudas.append(palabra)
               palabras_finales.remove(palabra)
               flagA = True
               continue
          
          # graves - acento en la penultima
          elif silaba[-2] in vocal_acento:
               clasificador.append("grave")
               graves.append(palabra)
               palabras_finales.remove(palabra)
               flagG = True
               continue

          # esdrujulas - siempre con acento
          elif any(palabra in vocal_acento for palabra in palabras):
               clasificador.append("esdrujula")
               esdrujulas.append(palabra)
               palabras_finales.remove(palabra)
               continue

     if flagA == False or flagG == False:
          for palabra in palabras_finales[:]:
               # para las agudas
               # Si la palabra termina en vocal, "n" o "s" y no lleva tilde 
               if palabra[-1] in vocales or palabra[-1] in ['n','s']:
                    clasificador.append("aguda")
                    agudas.append(palabra)
                    palabras_finales.remove(palabra)
                    continue
               
               # para las llanas o graves
               # llevan tilde en la penultima silaba
               if palabra[-1] not in ['n','s'] or palabra not in vocales:
                    clasificador.append("grave")
                    graves.append(palabra)
                    palabras_finales.remove(palabra)
                    continue
               
     return clasificador  

# -------------- main ---------------------------
file_name = "prueba.txt" 
file_name_mod = file_name.replace(".txt", "") # Elim
file_name_mod = file_name_mod + "m.txt" # Nombre del

mod_file = open("./Final/" + file_name_mod, 'w', encoding='utf-8') # Creo el acrchi
raw_file = open("./Final/" + file_name, 'r', encoding='utf-8') # Abro el archivo pa

for x in raw_file:  # normalizacion del texto
    xf = x.replace(".", "")
    xr = xf.replace(",", "")
    xs = xr.replace("(", "")
    xt = xs.replace(")", "")
    xu = xt.replace(":", "")
    xv = xu.replace(";", "")
    xw = xv.replace("¿", "")
    xx = xw.replace("?", "")
    xy = xx.replace("-", "")
    xz = xy.replace("!", "")
    xa = xz.replace("¡", "")
    xb = xa.replace("\"", "")
    xc = xb.replace("—", "")

    mod_file.write(xc)

mod_file.close()
raw_file.close()


# Contar lineas sin espacios y guardarlas--------
archivo = open("./Final/pruebam.txt", encoding='utf-8')

Content = archivo.read()
CoList = Content.split("\n")

for i in range (CoList.count('')):
    CoList.remove('')

resultado = []
palabras = []
finales = []
suma = 0
for line in CoList:
    text = line.split()
   
    finales.append(text[-1])    # guarda las ultimas palabras_finales de cada linea

    for word in text:   # separa las palabras_finales de cada oracion
        palabras.append(word)
        
    
for palabra in palabras:    # obtiene las silabas de las palabras de las oraciones
    resultado.append(syllabify(palabra))

# cuenta las silabas del poema 
for i in resultado:
    suma += len(i)

print("Sin las reglas, el poema tiene: ", suma, " silabas \n")

# separa las palabras en silabas
silabas_finales = []

for palabra in finales:
     silabas_finales.append(syllabify(palabra))

# determina el tipo de palabra de acuerdo a su silaba tónica
tipos = tipo_acentuacion(finales, silabas_finales)

# suma de acuerdo a las reglas
for tipo in tipos:
     if tipo == 'aguda' or tipo == 'monosilada':
          print("Termina en aguda, por lo que se suma 1 silaba")
          suma += 1
     elif tipo == 'grave':
          print("Termina en grave, por lo que se mantienen las silabas")
          suma += 0
     elif tipo == 'esdrujula':
          print("Termina en esdrujula, por lo que se resta 1 silaba")
          suma -= 1

print("\nEl poema tiene: ", suma , " silabas")


# Muestra las lineas con rimas consonantes$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
consonantes = []

print("++++++++++++++++++++++++++++++++ Rimas consonantes: +++++++++++++++++++++++++++++++++\n")

for j in range (len(CoList)-1):
    
    for k in range (len(CoList)-j-1):
        #print(j, j+k+1)
        
        if (CoList[j][-1] == CoList[j+k+1][-1]) and (CoList[j][-2] == CoList[j+k+1][-2]) and (CoList[j][-3] == CoList[j+k+1][-3]):
            #print(CoList[j])
            #print(CoList[j+k+1])
            if consonantes.count(CoList[j]) == 0:
                consonantes.append(CoList[j])
                
            if consonantes.count(CoList[j+k+1]) == 0:
                consonantes.append(CoList[j+k+1])
    consonantes.append(" ")

for l in range (len(consonantes)):
    print(consonantes[l])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



# Eliminacion de letras consonantes para obtener rimas asonantes %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
cpy = CoList
cpy2 = []
l_cons = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

for p in range(len(cpy)):
    texto = cpy[p]
    for letra in l_cons:
        texto = texto.replace(letra, "")
    
    cpy2.append(texto)

    #Invierte la cadena
    texto = texto[::-1]

#print(cpy2)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



# Muestra las lineas con rimas asonantes^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
asonantes = []

print("++++++++++++++++++++++++++++++++ Rimas asonantes: +++++++++++++++++++++++++++++++++\n")

for j in range (len(cpy2)-1):
    
    for k in range (len(cpy2)-j-1):
        #print(j, j+k+1)
        
        if (cpy2[j][-1] == cpy2[j+k+1][-1]) and (cpy2[j][-2] == cpy2[j+k+1][-2]):
            # print(CoList[j])
            # print(CoList[j+k+1])
            if (asonantes.count(CoList[j]) == 0): #and (consonantes.count(CoList[j]) == 0):
                asonantes.append(CoList[j])
                
            if (asonantes.count(CoList[j+k+1]) == 0): #and (consonantes.count(CoList[j+k+1]) == 0):
                asonantes.append(CoList[j+k+1])
    asonantes.append(" ")

for l in range (len(asonantes)):
    print(asonantes[l])
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

archivo.close()