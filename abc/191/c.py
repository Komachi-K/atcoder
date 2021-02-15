

# スペース区切りの整数の入力
h, w = map(int, input().split())

s = [[0] * w for _ in range(h)]

# N個の要素配列を入力
for i in range(h):
    s[i] = list(map(str,input()))
ans = 0

for i in range(h-1):

    for j in range(w-1):
        b_count = 0

        if s[i][j] == "#":
            b_count += 1
        if s[i+1][j] == "#":
            b_count += 1
        if s[i][j+1] == "#":
            b_count += 1
        if s[i+1][j+1] == "#":
            b_count += 1
        if (b_count%2) == 1:
            ans += 1 
print(ans)

