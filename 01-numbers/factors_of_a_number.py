"""
Find the number of factors for a given integer n.
Link : https://www.geeksforgeeks.org/problems/number-of-factors1435/1

 Examples:

Input: n = 5
Output: 2
Explanation: 5 has 2 factors 1 and 5

Constraints:
1 ≤ n ≤ 10^5
"""

def countFactors (n):
    count = 0
    for i in range (1,n+1):
        if (n % i == 0):
            count += 1
    return count            
inp_num = int(input("Enter the number : "))
num = inp_num
print(countFactors(num))

# Runtime Error 
# Test Cases Passed: 
# 1140 /2140
# Time limit exceeded.

# Your program took more time than expected.Expected Time Limit : 1.05sec

# we'll fix it on 15/06/2025 in factors_of_a_number_betterway.py
