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
    length = int_input()
    points = [0]*(length+1)
    array = list_input()
    for i,n in enumerate(array):
        points[n] = i
    
    lmax = 9999999999999999999999
    rmax = -1
    result = []
    for i in range(1,length+1):

        lmax = min(lmax,points[i])
        rmax = max(rmax,points[i])
        if rmax - lmax +1 ==i:
            result.append(1)
        else:
            result.append(0)
        
    print(*result)
