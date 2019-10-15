from math import gcd 
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_input =lambda : map(int, stdin.readline().split())
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

def dokarma(n):
    for i in range(1,n+1):
        if(degree[i] != 0):
            # seccond_flag = 0
            list_ = edgelist[i]
            for j in list_:
                answer[i-1] = 2
                answer[j-1] = 3
                # seccond_flag = 1
                return

edgelist = {}
degree = {}
answer = []
test = int_input()
for i in range(test):
    edgelist = {}
    n,m = multi_input()
    for i in range(m):
        u,v = multi_input()
        if u not in edgelist:
            edgelist[u] = [v]
        else:
            edgelist[u].append(v)
        if v not in edgelist:
            edgelist[v] = [u]
        else:
            edgelist[v].append(u)
    
    degree = {}
    for i in range(n):
        degree[i] = 0
    
    for i in edgelist:
        degree[i] = len(edgelist[i])
    
    answer = [1] * n

    if m%2 ==0:
        print(1)
        print(*answer)
    else:
        flag = 0
        for i in range(0,n):
            if(degree[i]%2!=0):
                #case for 2
                answer[i-1] = 2
                print(2)
                print(*answer)
                flag = 1
                break

        if(flag == 0):
            #case for 3
            print(3)
            dokarma(n)
            print(*answer)

