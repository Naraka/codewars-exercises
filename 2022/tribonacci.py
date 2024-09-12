# Bien conocido con el hermano mayor de Fibonacci, también conocido como Tribonacci.

# Como su nombre ya puede revelar, funciona básicamente como un Fibonacci, pero sumando los últimos 3 (en lugar de 2) números de la secuencia para generar el siguiente. Y, lo que es peor, lamentablemente no podré escuchar a hablantes no nativos de italiano tratando de pronunciarlo :(

# Entonces, si vamos a comenzar nuestra secuencia Tribonacci con [1, 1, 1] como entrada inicial (firma AKA), tenemos esta secuencia:

# [1, 1, 1, 3, 5, 9, 17, 31, ...]
# Pero, ¿y si comenzamos con [0, 0, 1] como firma? Como comenzar con [0, 1] en lugar de [1, 1] básicamente cambia la secuencia común de Fibonacci en un lugar, puede sentirse tentado a pensar que obtendríamos la misma secuencia desplazada en 2 lugares, pero ese no es el caso y obtendríamos:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Bueno, es posible que ya lo haya adivinado, pero para que quede claro: debe crear una función de Fibonacci que, dada una matriz/lista de firmas, devuelva los primeros n elementos, incluida la firma de la secuencia así sembrada.

# La firma siempre contendrá 3 números; n siempre será un número no negativo; si n == 0, devuelve una matriz vacía (excepto en C devuelve NULL) y prepárate para cualquier otra cosa que no esté claramente especificada;)

# Si disfrutaste de este kata, puedes encontrar una versión más avanzada y generalizada en el kata Xbonacci.

# [Agradecimiento personal al profesor Jim Fowler en Coursera por sus increíbles clases que realmente recomiendo a cualquier entusiasta de las matemáticas y por mostrarme esta curiosidad matemática también con su habitual pasión contagiosa :)]




def tribonacci(signature, n):
    signature=list(signature)
  
    calculator=list(signature)
    for i in range(n-3):
        calculator.append(sum(signature))
        signature.append(sum(signature))
        signature.pop(0)
    if n==0:
        print([])
    elif n == 1:
        print([signature[0]])
  
    elif n == 2:
        print([signature[0],signature[1]])
    else:
        print(calculator)

 #-------------------------------------------------------------------------------------------------------   
 #-------------------------------------------------------------------------------------------------------   



def tribonacci(signature,n):
    a,b,c = signature
    result = []
    for i in range(n):
        result.append(a)
        a,b,c = b,c,a+b+c
    print(result)


tribonacci([3,2,1], 10)