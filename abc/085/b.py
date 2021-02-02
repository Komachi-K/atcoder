
n = int(input())

d = list(range(n))

for i in range(n):
    d[i] = int(input())

d.sort(reverse=True)

count = 0
now_size = 0

for i in range(n):
    if now_size != d[i]:
        count += 1
    now_size = d[i]
    
print(count)


# import numpy as np

# n = int(input())
# d = list(range(n))

# for i in range(n):
#     d[i] = int(input())


# count = len(np.unique(d))

# print(count)
