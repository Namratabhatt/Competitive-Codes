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

a = list_input()

present = set([])
aldready = set([])

final = []
count = 0
flag = 0

for events in a:
    
    count+=1

    if events<0 and (-1*events) not in present:
        print(-1)
        flag = 1
        break
    elif events>0 and events not in present:
        if events not in aldready:
            present.add(events)
            aldready.add(events)
        else:
            print(-1)
            flag = 1
            break
    elif events<0 and (-1*events) in present:
        present.remove(-1*events)
        #print("Herer")
    if len(present) == 0:
        final.append(count)
        aldready = set([])
        count = 0
    #print(present)

if flag == 0:
    if len(present) == 0:
        print(len(final))
        print(*final)
    else:
        print(-1)