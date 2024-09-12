# Nuestro equipo de fútbol terminó el campeonato. El resultado de cada partido se ve como "x:y". Los resultados de todos los partidos se registran en la colección.

# Por ejemplo: ["3:1", "2:2", "0:1", ...]

# Escriba una función que tome tal colección y cuente los puntos de nuestro equipo en el campeonato. Reglas para contar los puntos de cada partido:

# si x > y: 3 puntos
# si x < y: 0 punto
# si x = y: 1 punto
# Notas:

# hay 10 partidos en el campeonato
# 0 <= x <= 4
# 0 <= y <= 4


def points(games):
    x=[]
    y=[]
    for i in games:
        x.append(i[0])
        y.append(i[2])

    a=[]
    for comp in range(0,10):
        if x[comp] > y[comp]:
            a.append(3)
        if x[comp] < y[comp]:
            a.append(0)
        if x[comp] == y[comp]:
            a.append(1)
            
    print(sum(a))

#--------------------------------------------------------------------------------------------------------

def points(a):
    print(sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a)))

#---------------------------------------------------------------------------------------------

def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    print(count)


        
        







games=['1:0','2:2','3:0','4:6','0:9','3:1','4:1','3:3','4:2','4:3']
points(games)













