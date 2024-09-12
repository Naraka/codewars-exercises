# Algunos números tienen propiedades divertidas. Por ejemplo:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Dado un entero positivo n escrito como abcd... (a, b, c, d... siendo dígitos) y un entero positivo p

# queremos encontrar un entero positivo k, si existe, tal que la suma de las cifras de n elevadas a las sucesivas potencias de p sea igual a k * n.
# En otras palabras:

# ¿Existe un número entero k como: (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# Si es el caso devolveremos k, si no devolveremos -1.

# Nota: n y p siempre se darán como números enteros estrictamente positivos.

# dig_pow(89, 1) debería devolver 1 ya que 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) debe devolver -1 ya que no hay k como 9¹ + 2² es igual a 92 * k
# dig_pow(695, 2) debería devolver 2 ya que 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) debería devolver 51 ya que 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


def dig_pow(n, p):

    count=p
    b=[]

    for i in str(n):
        a=int(i)**count
        b.append(a)
        count+=1

    if sum(b)%n ==0:
        print(sum(b)//n)
    else:
        print(-1)


    


dig_pow(46288 , 5)



