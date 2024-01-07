# Limpiar archivo de comas y puntos*****************************
file_name = "prueba.txt" 
file_name_mod = file_name.replace(".txt", "") # Elim
file_name_mod = file_name_mod + "m.txt" # Nombre del

mod_file = open("TLN/Final/" + file_name_mod, 'w') # Creo el acrchi
raw_file = open("TLN/Final/" + file_name, 'r') # Abro el archivo pa

for x in raw_file: 
    xf = x.replace(".", "")
    xr = xf.replace(",", "")
    xs = xr.replace("(", "")
    xt = xs.replace(")", "")
    xu = xt.replace(":", "")
    xv = xu.replace(";", "")

    mod_file.write(xv)

mod_file.close()
raw_file.close()
#****************************************************************



# Contar lineas sin espacios y guardarlas--------
archivo = open("TLN/Final/pruebam.txt", encoding='utf-8')

Content = archivo.read()
CoList = Content.split("\n")

for i in range (CoList.count('')):
    CoList.remove('')

#print(CoList)
#print(len(CoList))
#------------------------------------------------



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
            #print(CoList[j])
            #print(CoList[j+k+1])
            if (asonantes.count(CoList[j]) == 0): #and (consonantes.count(CoList[j]) == 0):
                asonantes.append(CoList[j])
                
            if (asonantes.count(CoList[j+k+1]) == 0): #and (consonantes.count(CoList[j+k+1]) == 0):
                asonantes.append(CoList[j+k+1])
    asonantes.append(" ")

for l in range (len(asonantes)):
    print(asonantes[l])
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


archivo.close()