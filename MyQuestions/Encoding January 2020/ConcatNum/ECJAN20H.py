n=int(input())
ans=0
a=input().split(' ')
maxLen=-1
buck=dict()
for i in a:
    l=len(i)
    if(l>maxLen):
        maxLen=l
    if buck.get(l):
        buck[l].append(i)
    else:
        buck[l]=[i]
ans=n-len(set(a)) 
#print(buck)
# input complete
#for i in a: # '123'
x=0
research=False
while x<len(a):
    l=len(i)# 3
    if research:
        searchLen=l
    else:
        searchLen=l-1
#    print("examining "+i+" searchLen "+str(searchLen))
    research=False
    for j in range(searchLen,0,-1):  #2 1 searching for substr of len j
#        print("searching in substr of len "+str(j))
        perms=l-j+1  #2 3
        for k in range(perms): # [0 1] [0 1 2]
            sub=i[k:k+j]
#            print("searching "+sub)
            if sub in buck[j]:
              #  0  2('12')
                i=i[0:k]+i[k+j:]
                if (i==''):
                    ans+=1
#                print("found, now searching for " + i)
                research=True
                break
        if research:
            break
    if not research:
        x+=1
        if x==len(a):
            break
        i=a[x]
#print("FINAL ANS " + str(ans))
print(str(ans))
