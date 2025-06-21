"""
Give one string and one list , Count the number of times the element which is present in q is appeared in s.
s = "azyxyyzaaaa"
q = ["d","a","y","x"]
Constraints : -
1. q <= s[i] <= z
"""

def hashing_bruteforce(str1,lst1):
    for element in lst1:
        count = 0
        for ch in str1:
            if ch == element:
                count += 1
        print(f"{element} : {count}")
if __name__ == "__main__":
    s = "azyxyyzaaaa"
    q = ["d","a","y","x"]
    hashing_bruteforce(s,q)