# Un pangrama es una oración que contiene todas las letras del alfabeto al menos una vez. Por ejemplo, la oración "El rápido zorro marrón salta sobre el perro perezoso" es un pangrama, porque usa las letras A-Z al menos una vez (el caso es irrelevante).

# Dada una cadena, detectar si es o no un pangrama. Devuelve True si lo es, False si no. Ignora los números y la puntuación.




def is_pangram(s):
    s=s.lower()
    alph="abcdefghijklmnopqrstuvwxyz"
    nose=[]
    for i in s:
        if i in alph:
            nose.append(i)

    if len(set(nose))==len(alph):
        print(True)
    else:
        print(False)












text="Tthe quick, brown fox jumps over the lazy dog!" #true
tex2="1bcdefghijklmnopqrstuvwxyz" #false


is_pangram(s=text)
is_pangram(s=tex2)