'''Dado un número entero, n , realice las siguientes acciones condicionales:
    Si es impar, imprime Raro
    Si es par y está en el rango inclusivo de 2 a 5 , imprime No Raro
    Si es par y está en el rango de 6 a 20 , imprime Raro
    Si es par y mayor que 20, imprime No Raro'''
for n in range(1,100):
    if(n%2 != 0):
        print(n," Raro")
    else:
        if((n>=2 and n<=5) or (n > 20) ):
            print(n," No rar0")
        else:
            print(n," Weird")


