from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
#from random import randint

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()

for _ in range(test):
    n,m = multi_int_input()
    weight = list_input()

    if m<n:
        print(-1)
    elif n==2:
        print(-1)
    else:
        fridge_list = []

        for i,k in enumerate(weight):
            fridge_list.append([k,i+1])
        
        sorted_fridges = sorted(fridge_list)

        first_pass = 0
        arrangement = []
        cost = 0

        for i in range(0,n-1):
            
            arrangement.append([i+1,i+2])
            cost+=weight[i]+weight[i+1]
            if i == n-2:
                arrangement.append([i+2,1])
                cost+=weight[i+1]+weight[0]

        if len(arrangement)<m:
            while(len(arrangement)<m):
                arrangement.append([sorted_fridges[0][1],sorted_fridges[1][1]])
                cost+=sorted_fridges[0][0]+sorted_fridges[1][0]
        
        print(cost)
        for i in arrangement:
            print(*i)
