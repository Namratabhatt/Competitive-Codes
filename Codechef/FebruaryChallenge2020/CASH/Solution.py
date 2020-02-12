from sys import stdin,stdout

intinp=lambda : int(stdin.readline())
multi_int =lambda : map(int, stdin.readline().split())
lstinp=lambda : list(map(int,stdin.readline().split()))

test = intinp()

for _ in range(test):
    n,k = multi_int()
    coins = lstinp()
    sumCoin = 0
    for i in coins:
        sumCoin+=(i%k)
    tolast = k - (coins[-1]%k)
    if sumCoin<tolast:
        print(sumCoin)
    else:
        mini = sumCoin - (coins[-1]%k)
        print((mini+coins[-1])%k)
