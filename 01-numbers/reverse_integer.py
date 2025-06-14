"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Link : https://leetcode.com/problems/reverse-integer/description/
 

Example 1:

Input: x = 123
Output: 321
"""

def reverse(n):
    is_negative = False
    if(n<0):
        is_negative = True
    n = abs(n)
    rvs_num = 0
    # length = len(str(n)) - 1
    # while (n > 0):
    #     last_digit = n % 10
    #     rvs_num += last_digit*(10**(length))
    #     length -= 1
    #     n = n//10

    # this while loops is wrong because of length variable, as it is getting converted into the string - is also counted while calculating the length

    while(n>0):
        last_digit = n % 10
        rvs_num = rvs_num * 10 + last_digit
        n = n // 10
    if (-2**31 >= rvs_num or rvs_num >= 2**31 - 1):
        return 0
    else :
        if is_negative:
            return -1*rvs_num
        else:
            return rvs_num
input_num = int(input("Enter the number : "))
num = input_num
reverse_num = reverse(num)
print(reverse_num)