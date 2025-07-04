"""
Yt video -- > https://www.youtube.com/watch?v=HKltpsIOOro&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=15&ab_channel=CodeandDebug

Find the factorial of a number using recursion
"""
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
if __name__ == "__main__":
    sample_input = 5
    print(factorial(sample_input))