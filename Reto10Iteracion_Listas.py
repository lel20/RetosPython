# -*- coding: utf-8 -*-
"""Reto_10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HW7pPgpVl1fX0DRuHB3b_sMDOmi6SIdT
"""

# Crear una una funcion que permita agregar en una sola lista de forma alterna los elementos de dos lista de la misma manera que se presenta a coninucaión:

# ["a","b","c","d"] ["a","b","c","d" ]= ['a', 1, 'b', 2, 'c', 3, 'd', 4]
#[1,2,3] [4,5,6]= [1,4,2,5,3,6]
#["h","o","l","a"] ["e","s","o"]= ["h","e","o","s","l","0","a"]

#Forma 1
def programa(list1, list2):
  result=[]
  for a,b in zip(list1,list2):
      result.append(a)
      result.append(b)
  return result
list1=["a","b","c","d"]
list2=[1,2,3,4,5]
resultado=programa(list1,list2)
print(resultado)


def programa(list1, list2):
  result=[]
  for i in range(0,max(len(list1),len(list2))):
    if i <len(list1) and i < len(list2):
      result.append(list1[i])
      result.append(list2[i])
    elif i < len(list1):
       result.append(list1[i])
    elif i < len(list2):
       result.append(list2[i])
  return result
list1=[5,6,7,8]
list2=[1,2,3,4]
resultado=programa(list1,list2)
print(resultado)