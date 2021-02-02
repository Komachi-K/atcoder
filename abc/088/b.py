
n = int(input())

# スペース区切りの整数の入力
a = list(map(int, input().split()))

Flag = 1

Alice_p = 0
diff = 0


Bob_p = 0
while Flag:
    if len(a) == 0:
        break
    max_value = max(a)
    max_index = a.index(max_value)
    # Alice_p += a.pop(max_index)
    diff += a.pop(max_index)
    if len(a) == 0:
        break
    max_value = max(a)
    max_index = a.index(max_value)
    # Bob_p += a.pop(max_index)
    diff -= a.pop(max_index)



print(diff)

# ################################################

# n = int(input())

# # スペース区切りの整数の入力
# a = list(map(int, input().split()))

# Flag = 1

# Alice_p = 0


# Bob_p = 0
# while Flag:
#     if len(a) == 0:
#         break
#     max_value = max(a)
#     max_index = a.index(max_value)
#     Alice_p += a.pop(max_index)
    
#     if len(a) == 0:
#         break
#     max_value = max(a)
#     max_index = a.index(max_value)
#     Bob_p += a.pop(max_index)

# diff = Alice_p - Bob_p

# print(diff)
