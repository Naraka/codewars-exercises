
 
def fumoRectangulos(l1, r1, l2, r2, l3, r3, l4, r4):
    x = 0
    y = 1

    ar1 = abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])
    ar2 = abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])
    ar3 = abs(l3[x] - r3[x]) * abs(l3[y] - r3[y])
    ar4 = abs(l4[x] - r4[x]) * abs(l4[y] - r4[y])
 
    distancia_x = (min(r1[x], r2[x], r3[x], r4[x]) - max(l1[x], l2[x], l3[x], l4[x]))
    distamcoa_y = (min(r1[y], r2[y], r3[y], r4[y]) - max(l1[y], l2[y], l3[y], l4[y]))
    print(distancia_x)
    print(distamcoa_y)
    area_fantasma = 0
    if distancia_x > 0 and distamcoa_y > 0:
        area_fantasma = distancia_x * distamcoa_y


    return (ar1 + ar2 + ar3+ ar4 - area_fantasma)
 

 
  
l1 = [2, 1]
r1 = [3, 3]
l2 = [4, 3]
r2 = [6, 5]
l3 = [5, 1]
r3 = [6, 6]
l4 = [1, 1]
r4 = [4, 5]
 
print(fumoRectangulos(l1, r1, l2, r2, l3, r3, l4, r4))
