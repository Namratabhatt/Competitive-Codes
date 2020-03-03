
# PROBLEM LINK:

[Practice](https://www.codechef.com/ENC2020/problems/ECFBP201)
[Encoding February 2020 Prelims](https://www.codechef.com/ENC2020)

***Author:***  [arnie8991](https://www.codechef.com/users/arnie8991)
***Tester:***  [nutella](https://www.codechef.com/users/nuttela)
***Editorialist:***  [arnie8991](https://www.codechef.com/users/arnie8991)

# DIFFICULTY:
CAKEWALK

# PREREQUISITES:
MATHS
 
# EXPLANATION:

This problem asks us to find the number of chocolates that will be left out. In order to find that we do a MOD operation which gives us the remainder of the chocolates

# SOLUTIONS:

[details="Setter's Solution"]

test = int(input())

for _ in range(test):
    a,b = map(int, input.split()) 
    print(a%b)

[details="Tester's Solution"]
