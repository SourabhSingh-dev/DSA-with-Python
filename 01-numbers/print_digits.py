"""
Problem: Print all the digits of a number
Approach: Use modulo (%) to extract digits and integer division (//) to reduce the number
Time Complexity: O(log₁₀n) or O(logn)
Space Complexity: O(1)
"""

def print_digits(num):
    while (num>0) :
        last_digit = num%10
        print(last_digit)
        num = num//10
given_num = int(input("Enter the number : "))
num_copy = given_num
print_digits(num_copy)        