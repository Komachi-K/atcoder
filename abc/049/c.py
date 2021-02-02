s = input()


while(s != ""):
    include_flag = 0
    if s[0:11] == "dreameraser":
        s = s[11:]
        include_flag = 1
    elif s[0:10] == "dreamerase":
        s = s[10:]
        include_flag = 1
    elif s[0:7] == "dreamer":
        s = s[7:]
        include_flag = 1
    elif s[0:5] == "dream":
        s = s[5:]
        include_flag = 1
    elif s[0:6] == "eraser":
        s = s[6:]
        include_flag = 1
    elif s[0:5] == "erase":
        s = s[5:]
        include_flag = 1
                    
    if include_flag == 0:
        break

if include_flag == 0:
    print("NO")
elif include_flag == 1:
    print("YES")

