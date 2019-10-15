
from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint

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
    pattern = string_input()
    flag = 0
    middleIndex = len(pattern)//2
    startingIndex = pattern.find('1')
    endingIndex = pattern.rfind('1')
    #print( middleIndex,startingIndex,endingIndex)
    if startingIndex == -1 or endingIndex == -1:
        flag = 1
    if(pattern[0] == '1' or pattern[-1] == '1'):
        print(n*2)
    elif (startingIndex<=middleIndex and (startingIndex+1) <=(len(pattern) - 1 - endingIndex) and flag == 0):
        print((n-startingIndex)*2)
    elif(endingIndex>=middleIndex and (len(pattern) -1- endingIndex)<=(startingIndex+1) and flag == 0):
        print((endingIndex+1)*2)
    elif(startingIndex+1 == middleIndex and endingIndex+1 == middleIndex):
        print(n+1)
    elif(flag == 1):
        print(n)