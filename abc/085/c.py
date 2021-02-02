n, y = map(int, input().split())

count_10000 = 0
count_5000 = 0
count_1000 = 0

ok_flag = 0

for i_10000 in range(n + 1):
    if ok_flag == 1:
        break
    for j_5000 in range(n - i_10000 + 1):

        if (i_10000 * 10000 + j_5000 * 5000 + (n - i_10000 - j_5000) * 1000) == y:
            print("{} {} {}".format(i_10000, j_5000, n - i_10000 - j_5000)) 
            ok_flag = 1
            break

if ok_flag == 0:
    print("-1 -1 -1")



# count_10000 = 0
# count_5000 = 0
# count_1000 = 0
# while(y >= 10000 and n > 0):
#     y -= 10000
#     n -= 1
#     count_10000 += 1

# while(y >= 5000 and n > 0):
#     y -= 5000
#     n -= 1
#     count_5000 += 1

# while(y >= 1000 and n > 0):
#     y -= 1000
#     n -= 1
#     count_1000 += 1

# if y != 0 or n < 0:
#     print("-1 -1 -1")
# else:
#     print("{} {} {}".format(count_10000,count_5000,count_1000))

