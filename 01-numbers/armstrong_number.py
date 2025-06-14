"""
Problem:
Given an integer n, check whether it is an Armstrong number.

A number is an Armstrong number if the sum of its digits raised to the power of the number of digits is equal to the number itself.

Link : From ChatGPT

🔹 Examples:
Test Case 1:
Input: n = 153
Output: True
Explanation: 1³ + 5³ + 3³ = 153
"""
def is_armstrong(n):
    if  n < 0:
        return False
    num = n
    length = len(str(num))
    digit_sum = 0
    while(num > 0):
        last_digit = num % 10
        digit_sum += last_digit**length
        num = num//10
    if (digit_sum == n):
        return True
    else:
        return False
inp_num = int(input("Enter the number : "))
num_copy = inp_num
print(is_armstrong(inp_num))