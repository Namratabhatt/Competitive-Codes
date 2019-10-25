import sys
import os
import random

# Python3 program to print all primes  
# smaller than n, using segmented sieve  
import math 

finalPrimes=[]
prime = [] 
  
# This method finds all primes  
# smaller than 'limit' using  
# simple sieve of eratosthenes.  
# It also stores found primes in list prime 
def simpleSieve(limit): 
      
    # Create a boolean list "mark[0..n-1]" and   
    # initialize all entries of it as True.  
    # A value in mark[p] will finally be False  
    # if 'p' is Not a prime, else True.  
    mark = [True for i in range(limit + 1)] 
    p = 2
    while (p * p <= limit): 
          
        # If p is not changed, then it is a prime  
        if (mark[p] == True):  
              
            # Update all multiples of p  
            for i in range(p * p, limit + 1, p):  
                mark[i] = False  
        p += 1
          
    # Print all prime numbers  
    # and store them in prime  
    for p in range(2, limit):  
        if mark[p]: 
            prime.append(p) 
            finalPrimes.append(p)
              
# Prints all prime numbers smaller than 'n'  
def segmentedSieve(n): 
      
    # Compute all primes smaller than or equal  
    # to square root of n using simple sieve 
    limit = int(math.floor(math.sqrt(n)) + 1) 
    simpleSieve(limit) 
      
    # Divide the range [0..n-1] in different segments  
    # We have chosen segment size as sqrt(n).  
    low = limit 
    high = limit * 2
      
    # While all segments of range [0..n-1] are not processed,  
    # process one segment at a time  
    while low < n: 
        if high >= n: 
            high = n 
              
        # To mark primes in current range. A value in mark[i]  
        # will finally be False if 'i-low' is Not a prime,  
        # else True.  
        mark = [True for i in range(limit + 1)] 
          
        # Use the found primes by simpleSieve()  
        # to find primes in current range  
        for i in range(len(prime)): 
              
            # Find the minimum number in [low..high]  
            # that is a multiple of prime[i]  
            # (divisible by prime[i])  
            # For example, if low is 31 and prime[i] is 3,  
            # we start with 33.  
            loLim = int(math.floor(low / prime[i]) * 
                                         prime[i]) 
            if loLim < low: 
                loLim += prime[i] 
                  
            # Mark multiples of prime[i] in [low..high]:  
            # We are marking j - low for j, i.e. each number  
            # in range [low, high] is mapped to [0, high-low]  
            # so if range is [50, 100] marking 50 corresponds  
            # to marking 0, marking 51 corresponds to 1 and  
            # so on. In this way we need to allocate space  
            # only for range  
            for j in range(loLim, high, prime[i]): 
                mark[j - low] = False
                  
        # Numbers which are not marked as False are prime  
        for i in range(low, high): 
            if mark[i - low]: 
                finalPrimes.append(i)
                  
        # Update low and high for next segment  
        low = low + limit 
        high = high + limit 
  
# Driver Code 
n = 100
print("Primes smaller than", n, ":") 
segmentedSieve(1000000)
print("Done") 

bigprimes=[123458177,12345681989,12345682043,123456792083,123456792293,853456806533,853456806239]
composites = [4,6,8,10,12,14,16,18,20,22,24,26,27,28,30,32,33,34,36,35,38,40]

N = 5
testfile = 5
for i in range(testfile):
    sys.stdout = open(os.path.join(sys.path[0],('testfile_input'+str(i)+'.in')),'w')
    noTestCases = 1
    #print(noTestCases)
    for j in range(noTestCases):
        lengthOfN = random.randrange(1,N)
        print(lengthOfN*2)
        array = []
        for k in range(lengthOfN*2):
            toss = random.choice([0,1])
            if toss == 1:
                array.append(random.choice(composites))
            else:
                toss = random.choice([0,1])
                if toss == 1:
                    array.append(random.choice(finalPrimes))
                else:
                    array.append(random.choice(bigprimes))
        print(*array)
    N*=10

