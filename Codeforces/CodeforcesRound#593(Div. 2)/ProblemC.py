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

n = int_input()

final = [0]*n
for i in range(n):
    final[i] = []

k = 0
count= 0
l = 0

for i in range(1,(n**2)+1):
    final[l].append(i)
    count+=1
    
    if count == n:
        count = 0
        if k == 0:
            k = 1
        else:
            k = 0
    else:
        if k == 0:
            l = (l+1)%n
        elif k == 1:
            l = (l-1)%n
    

for i in range(n):
    print(*final[i])