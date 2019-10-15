MOD = 1000000007

def fast_power(base, power):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result

r,c = map(int,input().split())
power = []
graph= []
count = 0
flag = 0
w = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
count = 0
for i in range(0,r):
    for j in range(0,c):
        if(i-h[j]<0 and j-w[i] == 0) or (j-w[i]<0 and i-h[j]==0):
            #print(i,j)
            flag = 1
        elif(i-h[j]>=1 and j-w[i]>=1):
            #print("free:",i,j)
            count+=1
if(flag == 0):
    print(fast_power(2,count))
else:
    print(0)