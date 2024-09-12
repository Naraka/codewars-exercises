# Completa la función de suma de cuadrados para que eleve al cuadrado cada número que se le pasa y luego suma los resultados.

# Por ejemplo, para [1, 2, 2] debería devolver 9 porque 1^2 + 2^2 + 2^2 = 9.




def square_sum(numbers):
    
    a=[]
    for i in numbers:
        numbers=i**2
        a.append(numbers)
    print(sum(a))



#--------------------------------------------------------------------------- 



def square_sum(numbers):
    return sum(x ** 2 for x in numbers)






numbers=[0,3,4,5]#50
square_sum(numbers)



