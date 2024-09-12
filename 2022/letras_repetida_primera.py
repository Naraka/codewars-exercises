# Escriba una función llamada first_non_repeating_letter que tome una entrada de cadena y devuelva el primer carácter que no se repite en ninguna parte de la cadena.

# Por ejemplo, si se le da la entrada 'stress', la función debería devolver 't', ya que la letra t solo aparece una vez en la cadena y aparece primero en la cadena.

# Como desafío adicional, las letras mayúsculas y minúsculas se consideran el mismo carácter, pero la función debe devolver el caso correcto para la letra inicial. Por ejemplo, la entrada 'sTreSS' debería devolver 'T'.

# Si una cadena contiene todos los caracteres repetidos, debería devolver una cadena vacía ("") o Ninguno; consulte las pruebas de muestra.





def first_non_repeating_letter(string):
    stra=string.lower()
    nose=""
    for i in stra:
        if stra.count(i)==1:
            nose+=i
            break

    if nose:

        for a in string:
            if a.lower()==i:
                print(a)
                break

    else:
        print("")


#--------------------------------------------------------------------------- 


def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):        #como enumerate tiene dos argumentos le añade i al primero y letter al segundo
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""









string="abba"
first_non_repeating_letter(string)

# string.isupper