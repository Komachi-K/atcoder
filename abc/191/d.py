# import numpy as np
# import math


# スペース区切りの整数の入力
x, y, r = map(float, input().split())

x = int(x*10000)
y = int(y*10000)
r = int(r*10000)

start_x = int(x - r)

end_x = int(x + r)
end_y = int(y - r)
start_y = int(y + r)

count = 0
right = 0
left = 0
# b = np.array([x, y])

# 第一象限（円を中心とする縦線と横線をを含む）
for i in range(start_y, y-1, -10000):
    j = x + right*10000
    loop_flag = True

    while loop_flag:
        d = int((x - i)**2 + (y - j)**2)

        if d <= r*r:
            right += 1
        else:
            loop_flag = False

        j += 10000


    count += right
right = 0

#第二象限（円を中心とする縦線をを含まない）
for i in range(start_y, y-1, -10000):
    j = x - left*10000 -10000
    loop_flag = True
    while loop_flag:
        d = int((x - i)**2 + (y - j)**2)

        if d <= r*r:
            left += 1
        else:
            loop_flag = False

        j -= 10000


    count += left
left = 0

#第三象限（円を中心とする縦線と横線をを含まない）
for i in range(end_y, y, 10000):
    j = x - left*10000 -10000
    loop_flag = True
    while loop_flag:
        d = int((x - i)**2 + (y - j)**2)

        if d <= r*r:
            left += 1
        else:
            loop_flag = False

        j -= 10000


    count += left
left = 0

# 第四象限（円を中心とする縦線を含む）
for i in range(end_y, y, 10000):
    j = x + right*10000
    loop_flag = True

    while loop_flag:
        d = int((x - i)**2 + (y - j)**2)

        if d <= r*r:
            right += 1
        else:
            loop_flag = False

        j += 10000


    count += right
right = 0

print(count)


# for j in range(start_y,end_y,10000):
#     for i in range(start_x,end_x,10000):
#         # a = np.array([i,j])
#         # u = b-a
#         d = int((x - i)**2 + (y - j)**2)
#         # d = np.linalg.norm(u)
#         # d = float(np.sqrt(a * a + b * b))
#         if d <= r*r:
#             count += 1
