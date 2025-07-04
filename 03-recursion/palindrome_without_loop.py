"""
Checking if a string is Palindrome or not
"""
def palindrome(l,r,s):
    if l > r:
        return True
    if s[l] != s[r]:
        return False
    return palindrome(l+1,r-1,s)
if __name__ == "__main__":
    sample_string = "abccvba"
    l = 0
    r = len(sample_string) - 1
    print(palindrome(l,r,sample_string))