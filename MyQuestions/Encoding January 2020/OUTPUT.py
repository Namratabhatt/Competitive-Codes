from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import sys
import os
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a)

def totient(n):
    c=0
    for i in range(1,n):
        if(gcd(i,n)==1):
            c+=1
    return c
test= 7
'''
for i in range(test):
    stdin = open(os.path.join(sys.path[0],'input'+str(i)+'.in'),'r')
    sys.stdout = open(os.path.join(sys.path[0],'output'+str(i)+'.in'),'w+') # input1.in
    #solution
    #start=t.time()
    for _ in range(int(input())):
        n=int(input())
        ans=totient(n)
        print(ans)
        #print(totient(n))
#print(t.time()-start)
        #Use single qoute to store in stdout
    #thats all
'''


stdin = open(os.path.join(sys.path[0],'input0.in'),'r')
sys.stdout = open(os.path.join(sys.path[0],'output0.in'),'w+') # input1.in
    #solution
    #start=t.time()
for _ in range(int_input()):
    n=int_input()
    ans=totient(n)
    print(ans)
