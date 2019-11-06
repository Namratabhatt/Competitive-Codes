from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
import os
import sys
#from random import randint
 
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7
#stdin = open(os.path.join(sys.path[0],"testB.in"),'r')
test = int_input()
 
for i in range(test):
    n = int_input()
    string1 = string_input()
    string2 = string_input()
 
    temp  = []
    count = 0
    for i in range(n):
        if string1[i]!=string2[i]:
            temp.append(i)
            count+=1
 
    #print(len(temp), *temp)
    if count ==2 and (string1[temp[0]] == string1[temp[1]] and string2[temp[1]] == string2[temp[0]]):
        print("Yes")
    else:
        print("No")
