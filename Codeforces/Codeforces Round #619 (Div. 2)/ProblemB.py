from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import ceil,floor

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

test = int_input()

for _ in range(test):
    n = int_input()
    arr = list_input()
    # crr = deepcopy(arr)
    brr = deepcopy(arr)
    brr.sort()
    brr = set(brr)
    brr = list(brr)
    avg = 0
    count = 0
    # print(brr)
    for i in brr:
        if i!= -1:
            avg+=i
            count+=1
    

    if count == 0:
        print(0,1)
    else:
        brr.sort()
        mini = brr[1]
        maxi = brr[-1]
        avg = mini+(maxi - mini)//2
        for i in range(len(arr)):
            if arr[i] == -1:
                arr[i] = avg
        ans = -99999
        for i in range(0, len(arr)-1):
            ans = max(ans,abs(arr[i] - arr[i+1]))

        # print(arr)
        print(ans,avg)
