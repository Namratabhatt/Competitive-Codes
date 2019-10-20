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

n = int_input()

length = list_input()

length = sorted(length)

queue = deque(length)

x = 0
y = 0

k = 0

while(len(queue)>0):
    #print(queue)
    if k%2 == 0:
        x += queue.pop()
    else:
        y += queue.popleft()
    k+=1

print(int(x*x +y*y))