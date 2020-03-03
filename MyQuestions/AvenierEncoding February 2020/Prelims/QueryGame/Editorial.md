
# PROBLEM LINK:

[Practice](https://www.codechef.com/ENC2020/problems/ECFBP204)
[Encoding Frbruary 2020 Prelims](https://www.codechef.com/ENC2020)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [nutella](https://www.codechef.com/users/nuttela)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
MEDIUM

# PREREQUISITES:
MATHS, Prefix
 
# EXPLANATION:

The easiest way to solve the problem is to figure out a way to compute the product query in O(1) time. To do this we use the concept of
prefix arrays. Suppose we have an array that has the numbers 1,2,3,4. The prefix array of products will then be 1,2,6,24. If we want to find the product of the last two numbers then we simply divide the last prefix product by the product just before the index from which we want our product. In this case its the index no 1 that holds 2. Hence our result is 24/2  = 12 which indeed is the product of 3 and 4.

one thing that needs to be noted is that fact that if zeroes are present in the subarray whose product we need to find, the answer is zero. Hence we need to take care about that condition. 

# SOLUTIONS:

[details="Setter's Solution]

    queries = int(input())

    clist = []
    previous = 1

    def add(n):
        global previous
        global clist
        if n == 0:
            clist = []
            previous = 1
            return
        previous = previous * n
        clist.append(previous)

    def getPro(n):
        if len(clist)<n:
            print(0)
            return
        ans = clist[-1]
        if len(clist) == n:
            print(ans)
        else:
            print(ans//clist[len(clist) - 1 - n])

    for _ in range(queries):
        typeQuery,n = multi_int_input()
        if typeQuery == 1:
            add(n)
        elif typeQuery == 2:
            getPro(n)

[details="Tester's Solution"]
