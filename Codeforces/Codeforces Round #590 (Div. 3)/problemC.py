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
dict_in = {}

id = list_input()
final_list = deque([])

for i in id:
    if i not in dict_in or dict_in[i] == 0:
        if(len(final_list)<k):
            final_list.appendleft(i)
            dict_in[i] = 1
        elif(len(final_list)>=k):
            a = final_list.pop()
            dict_in[a] = 0
            final_list.appendleft(i)
            dict_in[i] = 1

print(len(final_list))
print(*final_list)