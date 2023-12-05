'''
En un edifico hay una persona mayor que no puede bajar del ultimo piso  al primer  piso debido a que el asensor no funciona 
(el edificio no tiene escaleras).
Contruya un programaga que permita crear tantas escaleras como la señora necesite  para baja a la primera planta 
.
La salida del programa de verse de la siguiente manera:
  
[-]
[-][-]
[-][-][-]
[-][-][-][-]
'''

n=int(input('ingrese un valor'))
for elemnto in range (n):
    print('[-]'*elemnto)