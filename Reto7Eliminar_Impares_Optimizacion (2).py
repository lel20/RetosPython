#Elimine de la lista_original los numeros impares utilizando como apoyo la lista_auxiliar en menos de un segundo

import time
lista_original=list(range(1,1000001))
lista_auxiliar=range(1,1000001,2)
#lista_auxiliar=set(range(1,1000001,2)) con set se reduce mas el tiempo 
inicio=time.time()

####tu codigo aqui
new_list=[elementos for elementos in lista_original if elementos not in lista_auxiliar]

fin=time.time()
print(fin-inicio)