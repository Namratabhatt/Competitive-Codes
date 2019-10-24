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

N = int_input()

tree = {}
height = [0]*N

def dfs(tree,node,parent,level):
    #print("We are at node",node,"which is at level",level)
    height[level]+= len(tree[node])-1
    for children in tree[node]:
        if children!=parent:
            dfs(tree,children,node,level+1)

for i in range(N+1):
    tree[i] = []
tree[1].append(0)
for i in range(N-1):
    x,y = multi_int_input()
    tree[x].append(y)
    tree[y].append(x)

if len(tree) == 1:
    print(1)
else:
    dfs(tree,1,0,1)


maximum = max(height)

for i in range(0,len(height)):
    if height[i] == maximum:
        print(i+1)
        break