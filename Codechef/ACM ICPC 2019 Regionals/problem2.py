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

dicti = {}

def check(left,right,count,index):

test = int_input()

for _ in range(test):
    n = int_input()

    visited = {}
    #dicti = {}
    for i in range(n):
        left,right,speed = multi_int_input()

        dicti[i] = [left,right,speed,0]
    for i in range(n):
        visited[i] = False
    #print(dicti)
    for i in dicti[n]:

        dicti[i]
