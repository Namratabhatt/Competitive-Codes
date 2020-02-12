from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import ceil

# int_input=lambda : int(stdin.readline())
# string_input=lambda : stdin.readline().split()[0]
# multi_int_input =lambda : map(int, stdin.readline().split())
# multi_input = lambda : stdin.readline().split()
# list_input=lambda : list(map(int,stdin.readline().split()))
# string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7
lol = "abcdefghijklmnopqrstuvwxzy"
test = int(input())

for _ in range(test):
    string = input()

    if len(string) == 1:
        result= string
        for c in lol:
            if c != string:
                result+=c
        print("YES")
        print(result)
        
    else:
        dicti = {}
        for i in range(len(string)):
            if i!=r'\n':
                listi = []
                if i-1>=0:
                    listi.append(string[i-1])
                if i+1<len(string):
                    listi.append(string[i+1])
                if string[i] in dicti:
                    for items in listi:
                        dicti[string[i]].append(items)
                else:
                    dicti[string[i]] = listi

        flag = True
        count = 0
        for i in dicti:
            hehe = list(set(dicti[i]))
            dicti[i] = hehe
            # if len(hehe)>2 or (len(hehe) == 2 and (string[0] == i or string[-1] == i) and string[0]!=string[-1]):
                # flag = False
            if len(hehe) == 1:
                count+=1

        if count != 2:
            print("NO")
        else:
            added = set([])
            password = [-1]*len(dicti)
            # print(dicti)
            for i in dicti:
                if len(dicti[i]) == 1:
                    if password[0] == -1:
                        password[0] = i
                        password[1] = dicti[i][0]
                        
                    elif password[-1] == -1:
                        password[-1] = i
                        password[-2] = dicti[i][0]

                    added.add(i)
                    added.add(dicti[i][0])
            
            # print(password)
            ptr1,ptr2 = 1,-2
            while(len(added)!=len(dicti)):
                
                chars = dicti[password[ptr1]]
                for char in chars:
                    if char not in added:
                        password[ptr1+1] = char
                        ptr1+=1
                        added.add(char)

                chars = dicti[password[ptr2]]
                for char in chars:
                    if char not in added:
                        password[ptr2-1] = char
                        ptr2-=1
                        added.add(char)

            for c in range(97, 123): 
                if chr(c) not in added:
                    password.append(chr(c))
            # print(password)
            result = ""
            for i in password:
                result+=i
            print("YES")
            print(result)
