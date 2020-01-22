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
 
class coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
 
test = int_input()
 
for _ in range(test):
    n = int_input()
    listCoordinates = []
    for i in range(n):
        x,y = multi_int_input()
        listCoordinates.append(coordinate(x,y))
    
    flag = 0
    listCoordinates.sort(key = lambda y: y.x)
    prev = None
    # for i in range(0,len(listCoordinates)-1):
    #         p = listCoordinates[i]
    #         nextP = listCoordinates[i+1]
    #         if p.x == nextP.x and p.y > nextP.y:
    #             listCoordinates[i],listCoordinates[i+1] = listCoordinates[i+1],listCoordinates[i]
 
    for p in listCoordinates:
        if prev == None:
            prev = p
        else:
            if p.y<prev.y and p.x != prev.x:
                flag = 1
                break
        prev = p
    
    if flag == 1:
        print("NO")
    else:
        
        flag = 0
        dicti = {}
        for p in listCoordinates:
            if p.x in dicti:
                dicti[p.x].append(p.y)
            else:
                dicti[p.x] = [p.y]
 
        for points in dicti:
            if len(dicti[points])>1:
                dicti[points] = sorted(dicti[points])
 
        startingx = 0
        startingy = 0
        result = ""
        #print(dicti)
        for p in dicti:
            
            if len(dicti[p])>1:
                right = "R" * abs(startingx-p)
                up = "U" * abs(startingy - dicti[p][-1])
                if (startingy - dicti[p][0])>0:
                    flag = 1
                    break
                result+=right+up
                startingx = p
                startingy = dicti[p][-1]
                #print(len(dicti[p]),right,up, dicti[p])
            else:
                right = "R" * abs(startingx-p)
                up = "U" * abs(startingy - dicti[p][0])
                if (startingy - dicti[p][0])>0:
                    flag = 1
                    break
                result+=right+up
                startingx = p
                startingy = dicti[p][0]
                #print(len(dicti[p]),right,up,dicti[p][0])

        if flag == 0:
            print("YES")
            print(result)
        else:
            print("NO")