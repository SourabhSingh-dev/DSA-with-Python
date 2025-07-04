"""
Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes n as a parameter and prints the number from 1 to n recursively.

Note: Don't print any newline, it will be added by the driver code.

Examples:

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Input: n = 5
Output: 1 2 3 4 5
Input: n = 1
Output: 1
Constraints:
1 <= n <= 1000
"""
def printNos(n):
    if n == 0:
        return
    printNos(n-1)
    print(n,end=" ")
if __name__ == "__main__":
    sample_input = 10
    printNos(sample_input)