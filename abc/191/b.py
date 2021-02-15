# スペース区切りの整数の入力
n, x = map(int, input().split())

a = list(map(int, input().split()))  # n個の数字がリストに格納される


ans = []

# N個の要素配列を入力
for i in range(n):
    if a[i] != x:
        ans.append(a[i])

for i in range(len(ans)):
    print(ans[i], end = " ")

