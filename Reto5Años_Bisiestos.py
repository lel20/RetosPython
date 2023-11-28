'''Casi cada cuatro años se añade un día extra al calendario, como el 29 de febrero; y el día se llama día bisiesto. Corrige el calendario por el hecho de que nuestro planeta tarda aproximadamente 365,25 días en orbitar alrededor del sol. Un año bisiesto contiene un día bisiesto.
En el calensdario gregoriano se utilizan tres condiciones para identificar los años bisiestos:
El año que se puede dividir uniformemente entre 4, es bisiesto, a menos que:
    El año se puede dividir uniformemente entre 100, NO es año bisiesto, a menos que:
        El año también es divisible por 400. Entonces es un año bisiesto.
Esto significa que en el calendario gregoriano los años 2000 y 2400 son años bisiestos, mientras que 1800, 1900, 2100, 2200, 2300 y 2500 NO son años bisiestos. Fuente https://www.timeanddate.com/date/leapyear.html

Tarea:

Dado un año, determine si es bisiesto. Si es un año bisiesto, devuelva True, en caso contrario devuelva False.
Tenga en cuenta que el código auxiliar proporcionado lee STDIN y pasa argumentos a la función is_leap. Sólo es necesario completar la funcion is_leap.

La salida que debe mostra el programade ser de la siguiente manera:
    -True (si el año es 2000)
    -False (si el año el 1990)
    -True (si el año es 2400)
Asi sucesivamente
'''

def is_leap(year):
    leap = False
    if year % 4==0 and year % 400==0 and year % 100==0:
        leap =True
    elif year % 4==0 and year % 100==0:
        leap        
    elif year % 4 ==0:
        leap= True
    return leap
year = int(input("Ingrese el año"))
print(is_leap(year))