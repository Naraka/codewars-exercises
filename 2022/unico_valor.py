# Wfind_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# encontrar_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# Se garantiza que la matriz contiene al menos 3 números.

# Las pruebas contienen matrices muy grandes, así que piense en el rendimiento.

# Este es el primer kata de la serie:

# Encuentra el número único (este kata)
# Encuentra la cadena única
# Encuentra lo único










def find_uniq(arr):
    for i in set(arr):       #set siempre hace que se ejecute mas rapido el for
        a=arr.count(i)
        if a == 1:
            print(i)

#--------------------------------------------------------------------------- 



def find_uniq(arr):
        print(min(set(arr),key=arr.count))











find_uniq([ 1, 1, 1, 2, 1, 1 ])
find_uniq([ 0, 0, 0.55, 0, 0 ])
find_uniq([ 3, 10, 3, 3, 3 ])





