import math
from math import gcd 
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_input =lambda : map(int, stdin.readline().split())
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

n,k = multi_input()

id = list_input()
final_list = []

for i in id:
    if(i not in final_list and len(final_list)<k):
        final_list = [i]+final_list
    elif(i not in final_list and len(final_list)==k):
        final_list.pop(-1)
        final_list = [i]+final_list

print(len(final_list))
print(*final_list)