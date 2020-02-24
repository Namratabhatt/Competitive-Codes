from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
# from random import randint,randrange,choice
import heapq

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())

import os,sys

stdin = open(os.path.join(sys.path[0],'input1.in'),'r')
sys.stdout = open(os.path.join(sys.path[0],'output1.in'),'w')

row = col = int_input()

grid = []*row 

for i in range(row):
    grid.append(list_input())

dictionary = {}

for i in range(row):
    for j in range(col):
        if i-j not in dictionary:
            dictionary[i-j] = [0,[]]
            heapq.heapify(dictionary[i-j][1])

for i in range(row):
    for j in range(col):
        dictionary[i-j][0]+=grid[i][j]
        heapq.heappush(dictionary[i-j][1],grid[i][j])


maxi = None
high = -1000
key = None
for items in dictionary:
    print(items)
    if dictionary[items][0]>high:
        maxi = dictionary[items][1]
        high = dictionary[items][0]
        key = items


original = []
for i in range(row):
    for j in range(col):
        if i-j == key:
            original.append([grid[i][j],i,j])


# print(high)
# print(len(maxi))
while(len(maxi)>0):
    ele = heapq.heappop(maxi)
    for items in original:
        if items[0] == ele:
            print(items[1],items[2])



