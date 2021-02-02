
n = int(input())

a = list(map(int, input().split()))
count = 0
not_include_2 = 0



while 1:
    for i in a:
        if i%2 != 0:
            not_include_2 = 1
            
    if not_include_2 == 1:
        break
    
    for i in range(n):
        a[i] = a[i]/2
    count += 1
    
print(count)