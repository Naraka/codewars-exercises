# Bienvenidos.

# En este kata, se requiere que, dada una cadena, reemplace cada letra con su posición en el alfabeto.

# Si algo en el texto no es una carta, ignóralo y no lo devuelvas.

# "a" = 1, "b" = 2, etc

# Ejemplo
# alphabet_position("La puesta de sol se pone a las doce en punto").
# Debería devolver "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (como una cadena)






def alphabet_position(text):

    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    for a in "."," ","'":
        text=text.replace(a,"")
        

    text=text.lower()

    for i in text:
        if i in dict:
            text = text.replace(i,dict[i]+" ")
        

    text=text.split(" ")
    text.remove(text[-1])
    text=" ".join(text)
    print(text)

#-------------------------------------------------------------------------------------------------------   


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# ord()-96 da la posicion en el abecedario ya que ord() es la posicion en la lista de "unicode characters" la a es el 97-96== posicion 1 y asi
#

text="The sunset sets at twelve o' clock."
tex2="The narwhal bacons at midnight."
nose1=alphabet_position(text)
nose2=alphabet_position(text=tex2)























