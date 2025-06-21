"""
Using the benefit of constraints
a <= s[i] <= z
"""
def hashing_list(str1,lst1):
    hash_list = [0]*26
    for ch in str1:
        ascii_value = ord(ch)
        index = ascii_value-97
        hash_list[index] += 1
    for ch in lst1:
        ascii_value = ord(ch)
        index = ascii_value - 97
        print(f"{ch} : {hash_list[index]}")
if __name__ == "__main__":
    s = "azyxyyzaaaa"
    q = ["d","a","y","x"]
    hashing_list(s,q)