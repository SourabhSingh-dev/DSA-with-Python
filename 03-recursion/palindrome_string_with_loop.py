"""
You are given a sing s. Your task is to determine if the sing is a palindrome. A sing is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
Input: s = "a"
Output: true
Explanation: A single-character sing is always a palindrome.
Input: s = "acbca"
Output: true
Explanation: "acbca" reads the same forwards and backwards, so it is a palindrome.
"""
def isPalindrome(s):
    s = s.lower()
    left = 0
    right = len(s)-1
    while left < right :
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    else:
        return True
            
if __name__ == "__main__":
    sample_input = "abc"
    print(isPalindrome(sample_input))