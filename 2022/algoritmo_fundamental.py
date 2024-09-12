# Dados dos enteros a y b, que pueden ser positivos o negativos, encuentre la suma de todos los enteros entre ellos e incluyéndolos y devuélvalo. Si los dos números son iguales devuelve a o b.

# Nota: ¡a y b no están ordenados!

# Ejemplos (a, b) --> salida (explicación)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 ya que ambos son iguales)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# ALGORITMOS FUNDAMENTALES




def get_sum(a,b):

    nose=[]
    if a<b:
        
        for x in range(a,b+1):
            nose.append(x)
    
    else:
        for x in range(b,a+1):
            nose.append(x)

    print(sum(nose))

#--------------------------------------------------------------------------- 


def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))




get_sum(-1,2)






















