from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
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
    n = int_input()
    RPS = list_input()
    RPS_COPY = RPS
    sequence = string_input()
    win = 0
    winseq = ""
    for char in sequence:
        if char == 'R':
            if RPS[1]>0:
                RPS[1]-=1
                winseq += "P"
                win+=1
            else:
                winseq += "*"
        elif char == 'P':
            if RPS[2]>0:
                RPS[2]-=1
                winseq += "S"
                win+=1
            else:
                winseq += "*"
        elif char == 'S':
            if RPS[0]>0:
                RPS[0]-=1
                winseq += "R"
                win+=1
            else:
                winseq += "*"
        
    finalWINSeq = ""
    if win>=math.ceil(n/2):
        print("YES")
        for i in winseq:
            if i is not "*":
                finalWINSeq +=i
            else:
                if RPS[0]>0:
                    finalWINSeq +="R"
                    RPS[0]-=1
                elif RPS[1]>0:
                    finalWINSeq +="P"
                    RPS[1]-=1
                elif RPS[2]>0:
                    finalWINSeq +="S"
                    RPS[2]-=1
        print(finalWINSeq)
    else:
        print("NO")
        