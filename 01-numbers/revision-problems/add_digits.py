"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 
"""
def addDigits(num):
    if num < 10:
        return num
    while num >= 10 :
        sum = 0
        while num > 0 :
            last_digit = num % 10
            sum += last_digit
            num = num // 10
        num = sum
    return sum
if __name__ == "__main__":
    sample_input = 10
    print("Output : ",addDigits(sample_input))