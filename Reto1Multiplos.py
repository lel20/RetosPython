#Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
#* - Múltiplos de 5 por la palabra "buzz". #* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#for a in range(1,101):
#    multiplo3= a%3==0
#    multiplo5=a%5==0
#    if(multiplo3 and multiplo5):
#        print(f"{a}: fizzbuzz")
#    elif multiplo3:
#        print(f"{a}: fizz")
#    elif multiplo5:
#        print(f"{a}: buzz")
def multiplo():
    for a in range(1,101):
        if a%3==0 and a%5==0:
            print(f"{a}: fizzbuzz")
        elif(a%3==0):
            print(f"{a}: fizz")
        elif(a%5==0):
            print(f"{a}: buzz")
    
      
       
multiplo()    
    