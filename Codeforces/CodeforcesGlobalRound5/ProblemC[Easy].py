from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
 
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7
 
n = int_input()
 
pairs = {}
 
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i!=j):
            if ((i,j) not in pairs  and (j,i) not in pairs):
                pairs[(i,j)] = 0
 
coordinates = {}
#print(len(pairs))
for i in range(1,n+1):
    coordinates[i] = list_input()
 
# for keys in pairs:
for keys in pairs:
    dictance =   math.sqrt((coordinates[keys[0]][0] - coordinates[keys[1]][0])**2 + (coordinates[keys[0]][1] - coordinates[keys[1]][1])**2 + (coordinates[keys[0]][2] - coordinates[keys[1]][2])**2)
    pairs[keys] = dictance
 
output = {}
for i in range(1,n+1):
    output[i] = 0
 
for key, value in sorted(pairs.items(), key=lambda kv: kv[1] ):
    if output[key[0]] == 0 and output[key[1]] == 0:
        print(key[0],key[1])
        output[key[0]] = 1
        output[key[1]] = 1