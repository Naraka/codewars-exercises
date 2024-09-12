# El equipo de marketing dedica demasiado tiempo a escribir hashtags.
# ¡Ayudémoslos con nuestro propio Generador de Hashtags!

# Aquí está el trato:

# Debe comenzar con un hashtag (#).
# Todas las palabras deben tener su primera letra en mayúscula.
# Si el resultado final tiene más de 140 caracteres, debe devolver falso.
# Si la entrada o el resultado es una cadena vacía, debe devolver falso.
# Ejemplos
# "Hola, gracias por probar mi Kata" => "#HelloThereThanksForTryingMyKata"
# "Hola Mundo" => "#HolaMundo"
# "" => falso



def generate_hashtag(s):
    splited=s.split(" ")
    a=[]
  
    for i in splited:
        capi=i.capitalize()
        a.append(capi)
    result="".join(a)
  
    if len(result)==0:
        print(False)
    elif len(result)<140:
        print("#"+result)
    else:
        print(False)

    

    
#-------------------------------------------------------------------------------------------------------

def generate_hashtag(s): print( '#' +s.title().replace(' ','') if 0<len(s)<=140 else False)  #title pone en mayuscula cada una de las palbras dentro del string

#-------------------------------------------------------------------------------------------------------

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output






s="maricon            hijo        de puta  asd"

generate_hashtag(s)





