#Elimine de la lista_original los numeros impares utilizando como apoyo la lista_auxiliar en menos de un segundo
'''se te da la listta_normal que tiene un millon de elenento.
Crea un programa que permita extraer los primeros cien mil elementos de la lista proporcionada, en menos de un segundo
'''

import time
from collections import deque
lista_normal=[0]*1000000
inicio=time.time()

####tu código aqui
nueva_lista=deque(lista_normal)
for i in range(100000):
   nueva_lista.popleft()
###########

fin=time.time()
print(fin-inicio)