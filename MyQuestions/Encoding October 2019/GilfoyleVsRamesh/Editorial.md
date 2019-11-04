# PROBLEM LINK:

[Practice](https://www.codechef.com/ENOC2019/problems/GVR)
[Encoding October 2019 Contest](https://www.codechef.com/ENOC2019?order=desc&sortBy=successful_submissions)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [horsbug98](https://www.codechef.com/users/horsbug98)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
EASY

# PREREQUISITES:
[Rabin Miller primalty test](https://en.wikipedia.org/wiki/Miller–Rabin_primality_test)
 
# EXPLANATION:

The best approach to solve this problem quickly is to use the rabin miller primalty test to check which numbers are prime and then keep the count. 
You can read more about the Rabin Miller algorithm for primalty check and other similar algorithms from [here](https://cp-algorithms.com/algebra/primality_tests.html).
We have to individually count how many primes are there in the first half and the second half of the array and then decide whether the conditions are met or not.

# SOLUTIONS:

[details="Setter's Solution"]
    
    def check_composite(n, a, d, s):
        x = pow(a, d, n)
        if x==1 or x==n-1:
            return False
        for r in range(1, s):
            x = x * x % n
            if x==n-1:
                return False
        return True

    def miller_rabin(n):
        if n<2:
            return 0
        r = 0 
        d = n-1
        while((d&1)==0):
            d >>=1
            r += 1
        base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        for a in base:
            if n==a:
                return 1
            if check_composite(n, a, d, r):
                return 0
        return 1



    n = int(input())
    input_array = [int(x) for x in input().split()]

    first_prime = -2
    last_prime = -2

    leftCount = 0
    rightCount = 0

    for i in range(n//2):
        if (miller_rabin(input_array[i]) == 1):
            if first_prime == -2:
                first_prime = input_array[i]
            leftCount+=1

    for i in range(n//2,n):
        if (miller_rabin(input_array[i]) == 1):
            last_prime = input_array[i]
            rightCount+=1

    if (leftCount == rightCount and first_prime>last_prime):
        print('PERFECT')
    else:
        print('IMPERFECT')

[/details]
