"""
Problem: Count Digits That Divide a Number
Link: https://www.geeksforgeeks.org/problems/count-digits5716/1

Statement:
Given a positive integer n, count the number of digits in n that divide n evenly 
(i.e., n % digit == 0). 
Ignore any digit that is 0, as division by 0 is undefined.

Example:
Input: n = 122
Output: 2
Explanation: 1 and 2 divide 122 evenly.

Constraints:
1 <= n <= 10^5
"""
def evenlyDivides(n):
    num_copy = n
    count = 0
    while(num_copy > 0):
        last_digit = num_copy % 10
        if (last_digit != 0):
            if (n % last_digit == 0):
                count += 1
        num_copy = num_copy//10                
    return count

input_num = int(input("Enter the number : "))
num = input_num
even_digits = evenlyDivides(num)
print(even_digits)