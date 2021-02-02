 # スペース区切りの整数の入力
n, a, b = map(int, input().split())

sum1 = 0
sumAns = 0

for i in range(n):
    use_i= i+1
    lst = []
    while use_i > 0:
        lst.append(use_i%10)
        use_i //= 10 # 必須
    lst.reverse()
    sum1 = sum(lst)

    if a <= sum1:
        if b >= sum1:
            sumAns += (i+1)

print(sumAns)
