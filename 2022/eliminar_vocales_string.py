
#eliminar vocales de una string


string_="This website is for losers LOL!"

def disemvowel(string_):
    fra=[]
    for i in string_:
        if i in("a","e","i","o","u","A","E","I","O","U"):
            pass
        else:
            fra.append(i)


    
    joined="".join(fra)

    print(joined)


disemvowel(string_)

#-------------------------------------------------------------------------------------------------------   




def disemvowel(s):
    for i in "aeiouAEIOU": #si (i) es una vocal 
        s = s.replace(i,'') #remplazar por nada
    print(s)

frese="This website is for losers LOL!"
disemvowel(s=frese)





















