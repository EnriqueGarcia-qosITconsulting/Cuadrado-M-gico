""" 
Un cuadrado mágico es un cuadrado relleno de números cuya suma de sus filas, columnas y diagonales da siempre el mismo resultado
"""
#Función que comprueba si el cuadrado es mágico
def compruebaCuadradoMagico(cuadrado_Magico):
    esMagico = True
    sumaComparativa = 0 #Esta suma servirá para comparar las filas, columnas y diagonales del cuadrado
    suma = 0
    #Comprueba las filas
    for f in range(len(cuadrado_Magico)):
        suma = 0
        for c in range(len(cuadrado_Magico[f])):
            if f == 0:
                sumaComparativa += cuadrado_Magico[f][c]
            else:
                suma += cuadrado_Magico[f][c]
        if f > 0 and sumaComparativa != suma:
            esMagico = False
            return esMagico

    #Comprueba las columnas
    for f in range(len(cuadrado_Magico[f])):
        suma = 0
        for c in range(len(cuadrado_Magico)):       
            suma += cuadrado_Magico[f][c]
        if f > 0 and sumaComparativa != suma: 
            esMagico = False
            return esMagico
        
    #Comprueba la diagonal
    suma = 0
    for f in range(len(cuadrado_Magico)):
        suma += cuadrado_Magico[f][f]
    if sumaComparativa != suma:
        esMagico = False
        return esMagico
    
    #Comprueba la diagonal inversa
    suma = 0
    for f in range(len(cuadrado_Magico)):
        suma += cuadrado_Magico[len(cuadrado_Magico)-f-1][f]
    return esMagico

cuadrado_Magico = [4,9,2],[3,5,7],[8,1,6]
esMagico = compruebaCuadradoMagico(cuadrado_Magico)
print(esMagico)