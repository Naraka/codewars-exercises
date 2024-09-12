# Complete la solución para que devuelva verdadero si el primer argumento (cadena) pasado termina con el segundo argumento (también una cadena).

# Ejemplos:

# solution('abc', 'bc') # devuelve verdadero
# solution('abc', 'd') # devuelve falso






def solution(string, ending):
    item1=[]
    item2=[]
    for s in string:
        item1.append(s)
    for a in ending:
        item2.append(a)
    print(item1)
    
    verificar=[]
       
    for comp in range(-1,-len(ending)-1,-1): #en range se pone(donde empiezas,donde acabas,y como quieres llegar)
        if len(ending)>len(string):
            verificar.append(False)
            break

        if item1[comp]==item2[comp]:
            verificar.append(True)
        else:
            verificar.append(False)
        
    print(all(verificar))

    
#--------------------------------------------------------------------------- claro ejemplo de desconocimiento

# def solution(string, ending):
#     print(string.endswith(ending))


        
 
        
        

tring="abweqrwerwqrwerqwerwqerweqrcde"
nding="werwqerqwrqwerqwrcde"

solution(string=tring,ending=nding)















