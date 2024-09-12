
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!




my_list=["Keep", "Remove", "Keep", "Remove", "Keep"]

# def remove_every_other(my_list):
#      print(my_list[::2]) #eliminar cada segundo,cuarto,sexto etc elemento

# remove_every_other(my_list)



#-------------------------------------------------------------------------------------------------------


def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):     #en el rango de la longitud de la lista
        if i % 2 == 0:                  #si la posicion es par , la añade a r
            r.append(my_list[i])    #con esta forma de appen añadimos lo que hay en la lista pero segun la posicion que nos este dando i
    print(r)


remove_every_other(my_list)



