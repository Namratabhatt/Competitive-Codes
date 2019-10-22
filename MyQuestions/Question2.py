from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
#from random import randint
import sys

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

#solution
test  = int_input()

for _ in range(test): 
    tony = []
    thanos = []
    n,k = multi_int_input()
    #print(n,k)
    tony = list_input()
    thanos = list_input()

    list_numbers = []
    count_list = []
    li = deque(list_numbers)
    count_list = deque(count_list)

    present_elements = {}
    
    for i in range(0,n):
        #Tony's turn 
        if tony[i] not in present_elements or present_elements[tony[i]] == 0:
            if len(li) == k:
                x = li.popleft()
                present_elements[x] = 0
                count_list.popleft()  
            li.append(tony[i])
            count_list.append(1)
            present_elements[tony[i]] = 1
        
        #Thanos's turn
        if thanos[i] not in present_elements or present_elements[thanos[i]] == 0:
            if len(li) == k:
                x = li.pop()
                present_elements[x] = 0
                count_list.pop()  
            li.appendleft(thanos[i])
            count_list.appendleft(0)
            present_elements[thanos[i]] = 1
    
    no_tony = 0 
    no_thanos = 0

    for i in count_list:
        if i == 1:
            no_tony+=1
        elif i == 0:
            no_thanos+=1
    
    if no_tony>no_thanos:
        print('TONY')
    elif no_tony<no_thanos:
        print('THANOS')
    else:
        print('RUN TONY')
