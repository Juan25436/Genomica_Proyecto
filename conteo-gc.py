
import sys

"""
Verificamos que se provean los archivos FASTA como argumento a la hora de correr el script de python.

En caso de que no estén se lanzará un error y se mostrará mensaje 'Falta el archivo FASTA de entrada.'
"""
if len(sys.argv) != 2:
    raise ValueError('Falta el archivo FASTA de entrada.')

#Ya que sabemos el argumento fue dado, procedemos a abrirlo y extraer la información.
with open(sys.argv[1],'r') as f:
    data = f.read()

def conteo_gc(s1):
    """
    Función para realizar un conteo de elementos de Citocina y Guanina en una cadena.

    Parameters
    -----------
    s1: String.
    La cadena a analizar.

    Return
    ---------
    cc: int.
    El número de Citocina.

    cg: int.
    El número de Guanina.
    """
    cc = 0
    cg = 0
    for i in s1:
        if i == "C":
            cc += 1
        elif i == "G":
            cg += 1
    
    return cc,cg

def porcentaje(longitud,cc,cg):
    per = (cc+cg)/longitud
    return per

if __name__ == "__main__":
    a,b = conteo_gc(data)

    print("El conteo de C's:",end="")
    print(a)

    print("El conteo de G's:",end="")
    print(b)

    print("El porcentaje sería:",end="")
    print(porcentaje(len(data), a, b))