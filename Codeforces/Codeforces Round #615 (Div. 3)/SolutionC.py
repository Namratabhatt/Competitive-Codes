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
import math

test = int_input()
def solve(n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            a=i
            tmp=n//i
            for j in range(i+1, int(math.sqrt(tmp))+1):
                if(tmp%j==0 and (tmp//j!=a and tmp//j!=j)):
                    print("YES")
                    print(a,j,tmp//j)
                    return

    print("NO")
    return

for _ in range(test):

    n = int_input()

    solve(n)
    
    
    