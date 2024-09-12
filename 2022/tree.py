def dbl_linear(n):
    u = [1]
    v = 0
    s = 0
    while len(u) <= n:
        print(u)
        x = 2 * u[v] + 1
        y = 3 * u[s] + 1
        if x <= y:
            v += 1
        if x >= y:
            s += 1
        u.append(min(x,y))
    print(u)
    return u[n]


print(dbl_linear(20))