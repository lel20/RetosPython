
# Crear un progrma que, dada una lista, devuelva como resultado una lista con los valores paredes. Para ello tener encuenta las siguientes reglas:
# odd([1,2,3,4,5,6,7,8])=[2,4,6,8]
# odd([0,1,2,3,4,5,6,7,8])=[1,2,5,7]
# odd([])=[]
# odd([None, None, None])=[]
# odd([None,1,2,3,4,5,6,7,8])=[2,4,6,8]
# odd([None,1,2,None,3,4,5,6,7,8])=[2,4,6,8]
from ast import If
lista=[None,1,2,3,None,4,5,6,7,8]
lista1=([s for s in lista if s!=None])
resultado=[]

for i, li in enumerate(lista1):
  if i%2!=0:
   resultado.append(li)
print(resultado)
