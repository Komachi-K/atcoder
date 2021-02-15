v, t, s, d = map(int, input().split())

vanish = v * t
appear = v * s

ok_flag = 1

if vanish <= d <= appear:
    ok_flag = 0

if ok_flag == 1:
    print("Yes")
elif ok_flag == 0:
    print("No")