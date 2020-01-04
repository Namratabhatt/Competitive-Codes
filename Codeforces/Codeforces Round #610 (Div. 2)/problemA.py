from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
 
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7
 
test = int_input()
 
for _ in range(test):
    a,b,c,r = multi_int_input()
 
    left = c-r
    right = c+r
 
    if a == b:
        print(0)
    else:
        if a>b:
            a,b = b,a
        time = 0
        if left>a and right<b:
            time = ((left-a)+(b-right))
        elif left>b or right<a:
            time = abs(b-a)
        elif left<=a and right>=b:
            time = 0
        elif right>=b and left<=b:
            time = left-a
        else:
            time = b-right
        #print(left,right,b-a,time,a,b)
        print(time)