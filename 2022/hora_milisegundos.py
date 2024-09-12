# El reloj muestra h horas, m minutos y s segundos después de la medianoche.

# Su tarea es escribir una función que devuelva el tiempo desde la medianoche en milisegundos.

# Ejemplo:
# h = 0
# metro = 1
# s = 1

# resultado = 61000
# Restricciones de entrada:

# 0 <= hora <= 23
# 0 <= m <= 59
# 0 <= s <= 59


def past(h, m, s):
    print((s*1000)+((m*60)*1000+(h*3600000)))



#--------------------------------------------------------------------------- 




def past(h, m, s):
    return (3600*h + 60*m + s) * 1000



past(0,1,1)









