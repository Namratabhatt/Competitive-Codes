#######################################################################
#################### IMPORT LIBRARIES #################################
#######################################################################
 
from math import gcd 
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
import sys

#######################################################################
#################### STANDARD SNIPPETS ################################
#######################################################################

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7
sys.setrecursionlimit(2000)

#######################################################################
#################### ACTUAL CODE THAT MATTERS #########################
#######################################################################
tree = {0:[0],1:[]}
bacterias = [0]

def spreadBacteria(u,parent):
    #print("recieved values for parent and child is ",parent, " children",*children)
    for nodes in tree[u]:
        if nodes == parent:
            continue
        spreadBacteria(nodes,u)
    if (len(tree[u])>1 or (u == 1 and len(tree[u])>0)):
        bacterias[u] = 0
    bacterias[u]+=bacterias[parent]

n,q = multi_int_input()


for i in range(1,n):
    x,y = multi_int_input()
    if x not in tree:
        tree[x] = [y]
    else:
        tree[x].append(y)
    if y not in tree:
        tree[y] = [x]
    else:
        tree[y].append(x)

no_of_child_nodes = {}
bacterias = [0]
bacterias = bacterias + list_input()


for i in range(q):
    
    spreadBacteria(1,0)
    query = stdin.readline().split()
    if query[0] == '+':
        #spreadBacteria(1,0)
        index1 = int(query[1])
        index2 = int(query[2])
        bacterias[index1] += index2
    else:
        #spreadBacteria(1,0)
        print(bacterias[int(query[1])])