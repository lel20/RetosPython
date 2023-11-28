'''Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13'''

def fibonachi(numero:int):
    a=0
    b=1
    con=' '
    for valor in range(1,numero+1):
        con=con+str(a) +', '
        c=a+b
        a=b
        b=c
    print(con) 



fibonachi(50)