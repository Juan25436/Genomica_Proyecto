import numpy as np


def main():
    s1aux = input("Primera cadena\n")
    s2aux = input("Segunda cadena\n")
    s1 = leer_archivo(s1aux)
    s2 = leer_archivo(s2aux)
    #s1 = "CTTAGA"
    #s2 = "GTAA"
    input1 = np.array([c for c in s1])
    input2 = np.array([c for c in s2])
    aux = crear_matriz(input1, input2)
    print(aux[-1,-1,0])
    print(aux)
    #print(alinear(aux, input1, input2))

def crear_matriz(cadena1, cadena2):
    resultado = np.zeros((cadena1.size+1,cadena2.size+1,3))
    #esto inicializa la matriz
    i = 0
    while i <= cadena1.size:
        resultado[i,0,0] = i*(-2)
        i = i+1
    i = 0
    while i <= cadena2.size:
        resultado[0,i,0] = i*(-2)
        i = i+1
    #comenzamos a generar todos los valores, guardando la
    #referencia de la entrada que nos da el valor mas alto
    i = 1
    while i <= cadena1.size:
        j = 1
        while j <= cadena2.size:
            #si es match sumamos 1
            if cadena1[i-1] == cadena2[j-1]:
                resultado[i,j,0] = resultado[i-1,j-1,0] + 1
                resultado[i,j,1] = i-1
                resultado[i,j,2] = j-1
            #si cuesta mas el not match que el desplazamiento
            elif resultado[i,j-1,0] >= resultado[i-1,j-1,0] - 1 or resultado[i-1,j,0] >= resultado[i-1,j-1,0] - 1:
                #comparamos que desplazamiento conviene mas
                if resultado[i,j-1,0] >= resultado[i-1,j,0]:
                    resultado[i,j,0] = resultado[i,j-1,0] - 2
                    resultado[i,j,1] = i
                    resultado[i,j,2] = j-1
                else:
                    resultado[i,j,0] = resultado[i-1,j,0] - 2
                    resultado[i,j,1] = i-1
                    resultado[i,j,2] = j
            #caso donde no hay match pero unmatch es la mejor opcion
            else:
                resultado[i,j,0] = resultado[i-1,j-1,0] - 1
                resultado[i,j,1] = i-1
                resultado[i,j,2] = j-1
            j=j+1
        i=i+1
    return resultado

def alinear(matriz, c1, c2):
    resultado = ""
    cordenada1 = c1.size - 1
    cordenada2 = c2.size - 1
    #recorremos desde la ultima entrada el camino de referencias
    #guardando los match y poniendo lineas en indents
    while cordenada1 != 0 or cordenada2 != 0:
        if cordenada1 == (matriz[cordenada1,cordenada2,1] + 1) and cordenada2 == (matriz[cordenada1,cordenada2,2] + 1):
            resultado = c1[cordenada1] + resultado
        else:
            resultado = "-" + resultado
        cordenada1 = int(matriz[cordenada1,cordenada2,1])
        cordenada2 = int(matriz[cordenada1,cordenada2,2])
    return resultado

def leer_archivo(nombre):
    archivo = open(nombre,"r")
    lista = archivo.readlines()
    archivo.close()
    s_final = ''
    for i in lista:
        s_final = s_final + i
    return s_final

main()
