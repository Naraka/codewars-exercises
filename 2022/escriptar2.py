# El objetivo de este ejercicio es convertir una cadena en una nueva cadena donde cada carácter de la nueva cadena es "(" si ese carácter aparece solo una vez en la cadena original, o ")" si ese carácter aparece más de una vez en la original. cuerda. Ignore las mayúsculas al determinar si un carácter es un duplicado.

# Ejemplos
# "din" => "((("
# "retroceder" => "()()()"
# "Éxito" => ")())())"
# "((@" => "))(("
# notas
# Los mensajes de aserción pueden no estar claros acerca de lo que muestran en algunos idiomas. Si lee "... Debería codificar XXX", "XXX" es el resultado esperado, ¡no la entrada!





def duplicate_encode(word):
    word=word.lower()

    output=""
    for i in word:
        a=word.count(i)
        if a==1:
            output+=str("(")
        if a!=1:
            output+=str(")")


    print(output)

#-------------------------------------------------------------------------------------------------------   


# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
    








w="Success" #   )())())
w1="din" #      (((
w2="TlnWDgNVva" # (()((()))(
w3="maricon" 
w4="almenara" 
w5="farola" 
w6="fumador" 
duplicate_encode(word=w)
duplicate_encode(word=w1)
duplicate_encode(word=w2)
duplicate_encode(word=w3)
duplicate_encode(word=w4)
duplicate_encode(word=w5)
duplicate_encode(word=w6)