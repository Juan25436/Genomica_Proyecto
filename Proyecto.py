
import sys

"""
Verificamos que se provean los archivos FASTA como argumento a la hora de correr el script de python.

En caso de que no estén se lanzará un error y se mostrará mensaje 'Falta el archivo FASTA de entrada.'
"""
if len(sys.argv) != 3:
    raise ValueError('Falta el archivo FASTA de entrada.')

#Ya que sabemos el argumento fue dado, procedeoms a abrirlo y extraer la información.
with open(sys.argv[1],'r') as f:
    data = f.read()

with open(sys.argv[2],'r') as g:
    data2 = g.read()


def Hamming_Distance(s1,s2):
    """
    Función que implementa el algoritmo para encontrar la distancia de Hamming entre dos cadenas. 

    Parameters
    -----------
    s1: String.
    Primer cadena.

    s2: String.
    Segunda cadena.

    Return
    ---------
    indice: int.
    El indice que representa la distancia entre las cadenas.
    """
    indice = 0
    if (len(s1))!=(len(s2)):
        print("Error deben tener la misma longitud.")
        print(len(s1))
        print(len(s2))
    else:
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                indice += 1

    print(indice)
    return indice
                 
def Levinshtein_distance(s1,s2):
    """
    Función que implementa el algoritmo para encontrar la distancia de Levinshtein entre dos cadenas. Aquí se busca el minimo número de inserciones,sustituciones y cambios para que s1=s2. 

    Parameters
    -----------
    s1: String.
    Primer cadena.

    s2: String.
    Segunda cadena.

    Return
    ---------
    indice: int.
    El indice que representa la distancia entre las cadenas.
    """
    indice=0
    if len(s1)==0:
        indice = len(s2)
    elif len(s2)==0:
        indice = len(s1)
    elif s1[0]==s2[0]:
        Levinshtein_distance(s1[1:], s2[1:])
    else:
        indice += 1 + min(Levinshtein_distance(s1[0:],s2),Levinshtein_distance(s1, s2[0:]),Levinshtein_distance(s1[0:], s2[0:]))

    return indice

def distancia(s1,s2):
    """
    Función que calcula una distancia de una cadena a otra. Esto mediante la diferencia de longitudes entre cadenas y luego compara posición por posición los elementos.

    Parameters
    ----------
    s1: String.
    La primer cadena.

    s2: String.
    La segunda cadena.

    Return
    ---------
    indice: int.
    La distancia de un string a otro.
    """

    indice = 0
    if len(s1)<len(s2):
        indice = len(s2)-len(s1)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indice += 1
    
    if len(s2)<len(s1):
        indice = len(s1)-len(s2)
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                indice += 1
    
    if len(s2)==len(s1):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indice += 1

    return indice 


if __name__=="__main__":
    #Primero probemos con el primer algoritmo.
    """
    d = Hamming_Distance(data, data2)
    print(d)
    """
    #Probamos ahora con Levinshtein.
    """
    d = Levinshtein_distance(data,data2)
    print(d)
    """
    #Probamos con nuestra propuesta de distancia.
    d = distancia(data,data2)
    print(d)

