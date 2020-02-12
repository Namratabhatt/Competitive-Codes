test = int(input())

for _ in range(test):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    result = 0
    for i in range(n):
        result+=min(a[i],b[i])
    print(result)