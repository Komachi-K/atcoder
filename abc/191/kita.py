import math
# from decimal import *


def count(x, y, r):

    minx = (x - r) // 10000
    maxx = (x + r) // 10000
    cnt = 0

    for i in range(minx, maxx + 1):
        square = pow(r,2) - pow(x - i*10000, 2)


        if square >= 0:#内側

            root = math.isqrt(square)
            ymax = int((y + root) // 10000)
            ymin = int((y - root) // 10000)

            cnt += ymax - ymin 

    return cnt

X, Y, R = map(float,input().split()) 

X = round(X * 10000)
Y = round(Y * 10000)
R = round(R * 10000)
ans = 0

ans = count(X, Y, R)

print(ans)
