"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Link : https://leetcode.com/problems/palindrome-number/description/
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

def isPalindrome(num):
    # No need to consider the sign as it is not asked in question and dont use abs because of -121 it will become palindrome (See test cases)
    str_num = str(num)
    if (str_num[: :] == str_num[: : -1]):
        return True
    else : 
        return False
input_num = int(input("Enter the number : "))
num_copy = input_num
print(isPalindrome(num_copy))

# If you don't want to check palindrome using slicing then reverse the number and compare the reversed number with the original number.