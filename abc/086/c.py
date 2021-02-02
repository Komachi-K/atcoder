N = int(input())

t = list(range(N+1))
x = list(range(N+1))
y = list(range(N+1))

t[0] = 0
x[0] = 0
y[0] = 0
# N個の要素配列を入力
for i  in range(N):
    t[i+1], x[i+1], y[i+1] = map(int,input().split())

# print(N)
# print(t)
# print(x)
# print(y)

ok_flag = 1
for i in range(N):
    dt = t[i+1] - t[i]
    dxy = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    if dt < dxy:
        ok_flag = 0
    if dt%2 != dxy%2:
        ok_flag = 0 
    dt = dt
        
if ok_flag == 1:
    print("Yes")
elif ok_flag == 0:
    print("No")
    