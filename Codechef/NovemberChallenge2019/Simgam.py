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


def sum_of(array,index):
    sum = 0
    for i in range(index):
        sum+=array[i]
    return sum

test = int_input()

for _ in range(test):
    n = int_input()
    
    input_list = [0]*n
    for x in range(n):
        input_list[x] = list_input()
    
    c= [0]*n
    for i in range(n):
        c[i] = input_list[i][0]
        input_list[i] = input_list[i][1:]

    # print(*c)
    # print(*input_list)

    max_sum = 0
    odd_sums_frst= []
    odd_sums_last = []
    c_vals = []
    index_vals = []

    for i in range(n):
        if c[i]%2 == 0:
            max_sum+=sum_of(input_list[i],c[i]//2)
        else:
            temp = []

            temp.append(sum_of(input_list[i],(c[i]//2)+1))
            #temp.append(sum_of(input_list[i],c[i]//2))
            temp.append(i)
            odd_sums_frst.append(temp)

            temp = []
            temp.append(sum_of(input_list[i],c[i]) - sum_of(input_list[i],c[i]//2))
            temp.append(sum_of(input_list[i],c[i]) - temp[0])
            temp.append(i)
            odd_sums_last.append(temp)
            
    sorted_odd_sums = sorted(odd_sums_frst,reverse=True)
    sorted_odd_sums_last = sorted(odd_sums_last,reverse=True)
    # print(max_sum)
    # print(sorted_odd_sums)
    checker = {}
    for i in range(n):
        checker[i] = False
    k = l = 0
    for i in range(len(sorted_odd_sums)):
        if i%2 == 0:
            while(True):
                if checker[sorted_odd_sums[k][1]] == False:
                    max_sum += sorted_odd_sums[i][0]
                    checker[sorted_odd_sums[i][1]] = True
                    break
                else:
                    k+=1
        else:
            while(True):
                if checker[sorted_odd_sums_last[l][2]] == False:
                    max_sum += sorted_odd_sums_last[l][1]
                    checker[sorted_odd_sums_last[l][2]] = True
                    break
                else:
                    l+=1
        
        # print(max_sum)

        # #print(max_sum)

    print(max_sum)
    
    