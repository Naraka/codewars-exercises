# se le dará una serie de números. Tienes que ordenar los números impares en orden ascendente y dejar los números pares en sus posiciones originales.

# Ejemplos
# [7, 1] => [1, 7]
# [5, 8, 6, 3, 4] => [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] => [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]




def sort_array(source_array):

    odds = []
    answer = []
    
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
            
        else:
            answer.append(i)
            
    odds.sort()

    for i in odds:
        x = answer.index("X")  #asigna indice a X de odds 
        answer[x] = i           #en la posicion de la X pon i

        





    








arr=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sort_array(arr)









