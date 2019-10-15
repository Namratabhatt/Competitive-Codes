def check(number):
    list = []
    while(number>0):
        r = number%10
        number = number//10
        if(r not in list):
            list.append(r)
        else:
            return False
    return True

l,r = map(int,input().split())
flag = 0
for i in range(l,r+1):
    if check(i) == True:
        flag = 1
        print(i)
        break

if(flag == 0):
    print(-1)
    