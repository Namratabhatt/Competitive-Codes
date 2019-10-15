from math import gcd 
from collections import defaultdict, deque
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_input =lambda : map(int, stdin.readline().split())
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10;

def toDeci(str,base): 
    llen = len(str) 
    power = 1 #Initialize power of base 
    num = 0     #Initialize result 
    for i in range(llen - 1, -1, -1): 
        if val(str[i]) >= base: 
            #print('Invalid Number') 
            return -1
        num += val(str[i]) * power 
        power = power * base 
    return num

def all_possible_numbers_in_all_bases(number):
    
    list_of_numbers = []
    for i in range(2,37):
        copy = number
        X = toDeci(copy,i)
        if X<= 1000000000000 and X!= -1:
            list_of_numbers.append(X)
    #print(list_of_numbers)
    return list_of_numbers

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))  


test = int_input()
for i in range(test):
    n = int_input()
    listOfPossibleNumbers = []
    flag = 0
    for i in range(n):
        
        base,number = stdin.readline().split()
        base = int(base)
        if base == -1:
            if i == 0: 
                listOfPossibleNumbers = all_possible_numbers_in_all_bases(number)
            else:
                listOfPossibleNumbers = intersection(listOfPossibleNumbers,all_possible_numbers_in_all_bases(number))
        else:
            X = toDeci(number,base)
            if X>1000000000000:
                flag = 1
                
            else:
                
                if(len(listOfPossibleNumbers)!=0):
                    listOfPossibleNumbers = intersection([X],listOfPossibleNumbers)
                    if(len(listOfPossibleNumbers) == 0):
                        flag = 1
                elif(i == 0):
                    listOfPossibleNumbers.append(X)
    

    if(len(listOfPossibleNumbers) == 0 or flag == 1):
        print(-1)
    else:
        listOfPossibleNumbers = sorted(listOfPossibleNumbers)
        for i in listOfPossibleNumbers:
            if i!=-1:
                print(i)
                break



