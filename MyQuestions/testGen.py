import sys
import random

testfile = 5
k = 10
for i in range(testfile):
    sys.stdout = open('testfile_input'+str(i)+'.in','w')
    noTestCases = 5
    print(noTestCases)
    for j in range(noTestCases):
        N = random.randrange(5,k)
        K = random.randrange(2,k//2)
        print(N,K)
        list1 = []
        list2 = []
        for i in range(N):
            list1.append(random.randrange(1,N))
            list2.append(random.randrange(1,N))
        print(*list1)
        print(*list2)
    k*=10

        