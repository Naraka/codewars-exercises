# Un niño está jugando con una pelota en el piso n de un edificio alto. Se conoce la altura de este piso, h.

# Deja caer la pelota por la ventana. La pelota rebota (por ejemplo), a dos tercios de su altura (un rebote de 0,66).

# Su madre mira por una ventana a 1,5 metros del suelo.

# ¿Cuántas veces verá la madre pasar la pelota frente a su ventana (incluyendo cuando está cayendo y rebotando?

# Se deben cumplir tres condiciones para que un experimento sea válido:
# El parámetro flotante "h" en metros debe ser mayor que 0
# El parámetro flotante "rebote" debe ser mayor que 0 y menor que 1
# El parámetro flotante "ventana" debe ser menor que h.
# Si se cumplen las tres condiciones anteriores, devuelva un número entero positivo; de lo contrario, devuelva -1.

# Nota:
# La pelota solo se puede ver si la altura de la pelota que rebota es estrictamente mayor que el parámetro de la ventana.

# Ejemplos:
# - h = 3, rebote = 0,66, ventana = 1,5, el resultado es 3

# - h = 3, rebote = 1, ventana = 1.5, el resultado es -1





def bouncing_ball(h, bounce, window):

    if h>0 and bounce >0 and bounce <1 and window < h:


        contador=0
        while h >= window:
            h=h*bounce
            contador+=1
            if h==window:
                contador-=1
    
    
        print(contador*2-1)

    else:
        print(-1)








bouncing_ball(30,0.75,1.5)


