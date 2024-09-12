# Completa la función que

# acepta dos matrices enteras de igual longitud
# compara el valor de cada miembro en una matriz con el miembro correspondiente en la otra
# eleva al cuadrado la diferencia de valor absoluto entre esos dos valores
# y devuelve el promedio de la diferencia de valor absoluto al cuadrado entre cada par de miembros.
# Ejemplos
# [1, 2, 3], [4, 5, 6] --> 9 porque (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2] --> 16,5 porque (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1] --> 1 porque (1 + 1) / 2





def solution(array_a, array_b):

    mar=[]


    for i in range(len(array_a)):
        if array_a[i]>array_b[i]:
            mar.append((array_a[i]-array_b[i])**2)
        else:
            mar.append((array_b[i]-array_a[i])**2)
    
    print(sum(mar)/len(array_a))







a1 = [1,2,3]
a2 = [4,5,6]


solution(a1, a2)

