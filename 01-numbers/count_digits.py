'''
Problem statement
Ninja want to add coding to his skill set so he started learning it. On the first day, he stuck to a problem in which he has given a long integer ‘X’ and had to count the number of digits in it.

Ninja called you for help as you are his only friend. Help him to solve the problem.

Link: https://www.naukri.com/code360/problems/number-of-digits_4538242


EXAMPLE:
Input: 'X' = 2

Output: 1

As only one digit is ‘2’ present in ‘X’ so answer is ‘1’.
'''
def countDigit(n):
    count = 0
    if (n==0):
        return 1
    while (n > 0):
        count += 1
        n = n // 10
    return count
input_num = int(input("Enter the number : "))
num = input_num
digits = countDigit(num)
print(digits)