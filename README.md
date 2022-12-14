# Genomica_Proyecto

Aquí se encuentran nuestas secuencias analizadas para obtener la información que se encuentra en el pdf del proyecto, nuestros algoritmos creados para obtener o analizar dichas secuencias y también el pdf donde se explican nuestras conclusiones,resultados,objetivos entre otras cosas.


# Como correr nuestros programas.

## Conteo de GC.

Para esta parte de los resultados utilizamos el scrypt "conteo-gc.py".

Para correrlo, ya que estamos en una terminal en el directorio donde se encuentra el scrypt, se escribe lo siguiente en la terminal:

`python3 conteo-gc.py ./secuencias/<secuencia>.fna`

Y el programa automaticamente realizará el conteo de Citocina y Guanina en la cadena.

Imprimiendo en pantalla el conteo de Guanina,Citocina y el porcentaje GC dentro del genoma analizado.

## Distancia.

Para esta parte utilizamos el script "distancia.py" el cual fue creado con python 3.10 pero es compatible con cualquier 3.x. Para correrlo, se necesitan dos secuencias las que se quieren comparar entonces suponiendo que ya se está en el directorio donde se encuentra el scrypt "distancia.py" para correrlo se utiliza 

`$ python3 distancia.py ./secuencias/<secuencia1>.fna ./secuencias/<secuencia2>.fna`

Para facilitar la lectura de la información en los archivos FASTA se eliminaron los primeras lineas donde se encuentra el símbolo "<" ya que son lineas informativas y que no tienen parte de la secuencia del genoma.

En este scrypt hay distintos metodos codeados para calcular la distancia:

- Distancia de Hamming: Aquí, se calcula posición a posición los elementos de las cadenas. NO funciona si las cadenas tienen longitudes distintas. Como ocurre con nuestras cadenas.

- Distancia de Levinshtein: Aquí, las cadenas pueden tener longitudes diferentes y esta distancia busca el menor número de inserciones, sustituciones y cambios de la cadena 1 para que sea igual a la cadena 2. NO funciona con cadenas muy grandes porque al menos en python manda el error donde se llega al "maximum recursion depth".


- distancia(nuestra propuesta): Si las cadenas son de distintos tamaños calculamos la diferencia de longitudes y luego comparamos posición a posición los elementos que sí comparten. También calculamos las veces que sí comparten el mismo elemento en la misma posición. 

Para probar las distintas formas de calcular la distancia o el indice de similitud solo se deben descomentar las partes del final del script donde se tiene:

`d = [Levinshtein_distance | Hamming_Distance](data,data2)`

La imagen siguiente indica donde se tienen que descomentar para utilizar las diferentes formas:

![indice](/images/indice.png)

## Alineamiento.

Para esta seccion usamos el script "Needleman-Wuntch.py" para ejecutarlo utilizamos el comando en terminal

`$ python3 Needleman-Wuntch.py`
 
La terminal solicitara dos entradas que corresponden a los nombres de los dos archivos que contengan los genomas, estos deben encontrarse en el mismo directorio que el script y de manera similar a los scripts pasados, se elimina la primera linea de los archivos FASTA que utilicemos

La ejecucion puede tomar tiempo, pero una vez concluye devuelve el puntaje que se encuentre en la casilla inferior derecha de la matriz generada por dicho algoritmo

Para cambiar la cantidad de nucleotidos con los que trabajara el programa, basta cambiar en la linea

`for i in range(200):`

el valor 200 por el valor deseado (el valor no esta dado en nucleotidos, esta en lineas de los archivos FASTA que contien cadenas de tamaño 80 )
