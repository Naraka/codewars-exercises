# Hubo un examen en tu clase y lo pasaste. ¡Felicidades!
# Pero eres una persona ambiciosa. Quiere saber si es mejor que el estudiante promedio de su clase.

# Recibe una matriz con los puntajes de las pruebas de sus compañeros. ¡Ahora calcule el promedio y compare su puntaje!

# ¡Devuelve True si estás mejor, de lo contrario False!

# Nota:
# Sus puntos no están incluidos en la matriz de puntos de su clase. ¡Para calcular el punto promedio, puede agregar su punto a la matriz dada!


def better_than_average(class_points, your_points):
    if your_points < (sum(class_points)/len(class_points)):
        print(False)
    else:
        print(True)
    print(sum(class_points))

#--------------------------------------------------------------------------- 



def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)



class_points=[23, 7, 33, 23, 82, 61, 78, 97, 53, 59, 47, 84, 53, 53, 60, 90, 17, 43, 89, 89, 39, 82, 48, 2, 7, 48, 21, 53, 17, 17, 61, 88, 29, 4, 69, 11, 37, 28, 96, 28, 4, 67, 72, 89, 11, 96, 14, 58, 69, 56]
your_points=52



better_than_average(class_points,your_points)





