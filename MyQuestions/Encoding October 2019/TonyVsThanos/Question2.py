from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
#from random import randint
import sys
import os

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

# testfiles = 5
# for i in range(testfiles):
#     stdin = open('testfile_input'+str(i)+'.in','r')
#     sys.stdout = open('testfile_output'+str(i)+'.in','w')

# stdin = open(os.path.join(sys.path[0],'testfile_input5.in'),'r')
# sys.stdout = open(os.path.join(sys.path[0],'testfile_output5.in'),'w')
#solution

from collections import deque

test  = int(input())

for _ in range(test): 
    tony = []
    thanos = []
    n,k = map(int,input().split())
    #print(n,k)
    tony = [int(x) for x in input().split()]
    thanos = [int(x) for x in input().split()]

    list_numbers = []
    li = deque(list_numbers)

    present_elements = {}

    no_tony = 0 
    no_thanos = 0
    
    for i in range(0,n):
        #Tony's turn 
        if (tony[i] not in present_elements or present_elements[tony[i]] == 0):
            if len(li) == k and no_thanos>0:
                x = li.popleft()
                present_elements[x] = 0
                no_thanos-=1
            if(len(li)<k):
                li.append(tony[i])
                no_tony+=1
                present_elements[tony[i]] = 1
            
        #Thanos's turn
        if (thanos[i] not in present_elements or present_elements[thanos[i]] == 0):
            if len(li) == k and no_tony>0:
                x = li.pop()
                present_elements[x] = 0
                no_tony-=1
            if(len(li)<k):
                li.appendleft(thanos[i])
                no_thanos+=1
                present_elements[thanos[i]] = 1
            
        # print(li)
        # print(present_elements)
        # print(count_list)

    if no_tony>no_thanos:
        print('TONY')
    elif no_tony<no_thanos:
        print('THANOS')
    else:
        print('RUN TONY')
