from sys import stdin,stdout

intinp=lambda : int(stdin.readline())
multi_int =lambda : map(int, stdin.readline().split())
lstinp=lambda : list(map(int,stdin.readline().split()))

test = intinp()

for _ in range(test):
    
    l,k = multi_int()
    coins = lstinp()
    coins2 = coins
    coins2.sort()

    defect1,defect2 = -1,-1
    flag = False
    lol = -1
    for i in range(0,len(coins2)):
        if k%coins2[i]!=0:
            flag = True
            lol = coins2[i]
            break
        for j in range(i+1,len(coins2)):
            #print(coins2[i],coins2[j])
            if coins2[j]%coins2[i]!=0:
                defect1 = coins2[i]
                defect2 = coins2[j]
                break
    ans = []
    if(flag == True):
        for i in coins:
            if i == lol:
                ans.append(k//lol+1)
            else:
                ans.append(0)
        print("YES",*ans)
    elif defect1 != -1 and defect2 != -1:
        maxi = max(defect1,defect2)
        mini = min(defect1,defect2)
        ans1 = k//maxi - 1
        k = k - (k//maxi-1)*maxi
        ans2  = k//mini+1
        for i in coins:
            if i == maxi:
                ans.append(ans1)
            elif i == mini:
                ans.append(ans2)
            else:
                ans.append(0)
        print("YES",*ans)
    else:
        print("NO")
        
    