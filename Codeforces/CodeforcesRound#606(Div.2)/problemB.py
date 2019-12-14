from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
import heapq

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
    brr = []
    arr= set(arr)
    crr = []
    for elements in arr:
        if elements%2 == 0:
            brr.append(-1*elements)
            crr.append(-1*elements)

    crr = set(crr)
    heapq.heapify(brr)
    count = 0
    #print(arr)
    while(len(brr)>0):
        maxi = heapq.heappop(brr)
        new = maxi//2
        if new %2 ==0 and new not in crr:
            #print(arr,new)
            heapq.heappush(brr,maxi//2)
            #print(brr)
        count+=1
    print(count)