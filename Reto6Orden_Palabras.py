'''Te dan n palabras. Algunas palabras pueden repetirse. Para cada palabra, genere su número de apariciones. El orden de salida debe corresponder con el orden de entrada de aparición de la palabra. Consulte el ejemplo de entrada/salida para obtener más aclaraciones.

Formato de entrada

La primera línea contiene el número entero, n.
Las líneas siguentes contiene cada palabra de acuerdo al n.

Formato de salida

Producción 2 líneas.
En la primera línea, genere el número de palabras distintas de la entrada.
En la segunda línea, genere el número de apariciones de cada palabra distinta según su aparición en la entrada.


Entrada de muestra

4
bcdef
abcdefg
bcde
bcdef

Salida de muestra

3
2 1 1
Explicación

Hay 3 palabras distintas. Aquí, "bcdef" aparece dos veces en la entrada; en la primera y última posición. Las otras palabras aparecen una vez cada una. El orden de las primeras apariciones es "bcdef" , "abcdefg" y "bcde" , que corresponde a la salida.
'''

n=int(input("Cantidad de Palabras: "))
arreglo={}
for a in range(n):
    palabra=(input("Ingrese la palabra: "))
    if palabra in arreglo:
        arreglo[palabra]+=1
    else:
        arreglo[palabra]=  1
print(len(arreglo))
print(*arreglo.values())
