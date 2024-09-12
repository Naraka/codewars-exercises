# Construye una torre en forma de pirámide dado un número entero positivo de pisos. Un bloque de pisos se representa con el carácter "*".
# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]




def tower_builder(n_floors):
    if n_floors == 0:
        return []

    result = []

    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        result.append(space + stars + space)
    
    print(result)


tower_builder(4)



  



