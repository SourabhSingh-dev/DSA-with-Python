"""
Given a number n, determine whether it is a prime number or not.

A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Link : https://www.geeksforgeeks.org/problems/prime-number2314/1

Examples :

Input: n = 7
Output: true
Explanation: 7 has exactly two divisors: 1 and 7, making it a prime number.
Input: n = 25
Output: false
Explanation: 25 has more than two divisors: 1, 5, and 25, so it is not a prime number.
Input: n = 1
Output: false
Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.
Constraints:
1 ≤ n ≤ 109
"""
import math
def isPrime(n):
    if n == 1 or 0:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    else:
        return True
if __name__ == "__main__":
    sample_input = 1
    print("Output : ",isPrime(sample_input))