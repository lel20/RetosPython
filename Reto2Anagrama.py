def  anagrama(palabra1:str, palabra2:str):
     mensaje1='Es un anagrama'
     mensaje2='No es un anagrama'
     if palabra1==palabra2:
         return mensaje2
     elif len(palabra1)==len(palabra2):
        a=0
        for letra in palabra1:
            if letra in palabra2:
                a+=1
        if a==len(palabra1):
            return mensaje1
        else:
             return mensaje2
     else:
        return mensaje2
    
    
print(anagrama("eso","oe"))