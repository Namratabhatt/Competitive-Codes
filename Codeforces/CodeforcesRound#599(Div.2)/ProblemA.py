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

#stdin = open(os.path.join(sys.path[0],"testA.in"),'r')


test = int_input()

for _ in range(test):
    n = int_input()

    tiles = list_input()

    sorted_tiles = sorted(tiles,reverse = True)

    final = []

    for i in range(len(sorted_tiles)):
        final.append(min(i+1,sorted_tiles[i]))

    print(max(final))
