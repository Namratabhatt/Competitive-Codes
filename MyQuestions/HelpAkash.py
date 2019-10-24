# from collections import defaultdict, deque
# from itertools import permutations
# from sys import stdin,stdout
# from bisect import bisect_left, bisect_right
# from copy import deepcopy
# #from random import randint

# int_input=lambda : int(stdin.readline())
# string_input=lambda : stdin.readline()
# multi_int_input =lambda : map(int, stdin.readline().split())
# multi_input = lambda : stdin.readline().split()
# list_input=lambda : list(map(int,stdin.readline().split()))
# string_list_input=lambda: list(string_input())
# MOD = pow(10,9)+7

# try:
#     test = int_input()

#     for i in range(test):
#         N = input()
#         if len(N) == 1:
#             print(N)
#         elif len(N) == 2:
#             print(int(N[0])^int(N[0]))
#         else:
#             xor = ""
#             narray = []
#             for ch in N:
#                 narray.append(int(ch))
#             #print(narray)
#             for pos in range(0,len(narray)):
#                 xor+=str(narray[pos]^narray[(pos+1)%len(N)])
#             print(xor)
# except:
#     pass

# # for i in range(test):
# #     N = string_input()
# #     xor = ""
# #     narray = N[0:-1]
# #     length = len(narray)
# #     for pos in range(0,length):
# #         if pos == length-1:
# #             xor+=str(int(narray[pos])^int(narray[0]))
# #         else:
# #             xor+=str(int(narray[pos])^int(narray[pos+1]))
# #     print(xor)

# # for _ in range(int(input())):
# #     n=list(input())
# #     a=[int(i) for i in n]
# #     ans=''
# #     for i in range(len(a)-1):
# #         ans+=str(a[i]^a[i+1])
# #     if(len(a)>2):
# #         ans+=str(a[0]^a[-1])
# #     if(len(a)==1):
# #         ans=a[0]
# #     print(ans)


for _ in range(int(input())):
    n=list(input())
    a=[int(i) for i in n]
    ans=''
    for i in range(len(a)-1):
        ans+=str(a[i]^a[i+1])
    if(len(a)>2):
        ans+=str(a[0]^a[-1])
    if(len(a)==1):
        ans=a[0]
    print(ans)
