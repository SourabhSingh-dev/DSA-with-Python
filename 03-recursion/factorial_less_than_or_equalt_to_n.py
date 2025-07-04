"""
A number n is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120,
Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.

Examples:

Input: n = 3
Output: 1 2
Explanation: The first factorial number is 1 which is less than equal to n. The second number is 2 which is less than equal to n,but the third factorial number is 6 which is greater than n. So we print only 1 and 2.
Input: n = 6
Output: 1 2 6
Explanation: The first three factorial numbers are less than equal to n but the fourth factorial number 24 is greater than n. So we print only first three factorial numbers.
Constraints:
1<=n<=1018
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
def main_func(num):
    if num == 0:
        return
    f = factorial(num)
    if f <= num:
        print(f)
    main_func(num -1 )
main_func(3)