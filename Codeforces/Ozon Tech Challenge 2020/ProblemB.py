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

string = input()

def check(s):
    x = False
    for ch in s:
        if ch == '(':
            x = True
        if ch == ')' and x == True:
            return True
    return False

final_ans = []
dicti = {'(':[],')':[]}
stack = []

if check(string) == False:
    print(0)
else:
    while(check(string)):
        arr = []
        ans = []
        for i in range(len(string)):
            ch = string[i]
            if ch == '(':
                arr.append(i)
        #print(arr)
        ptr = 0
        for i in range(len(string)-1,-1,-1):
            ch = string[i]
            if ch == ')' and ptr<len(arr) and arr[ptr]<i:
                
                ans.append(arr[ptr])
                ans.append(i)
                ptr+=1

        ans.sort()
        final_ans.append([len(ans),ans])
        newStr = ""
        for i  in range(len(string)):
            if i not in ans:
                newStr += string[i]
    
        string = newStr
        

    print(len(final_ans))
    for i in final_ans:
        print(i[0])
        for i in i[1]:
            print(i+1,end = " ")
        print()



