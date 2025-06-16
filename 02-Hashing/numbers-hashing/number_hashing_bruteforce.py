"""
Give two lists n and m , Count the number of times the element which is present in m is appeared in n.
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
Constraints : -
1. 1 <= n[i] <= 10
2. n can have 10^8 elements
3. m can have 10^8 elements
"""

def hashing_numbers(lst1,lst2):
    for num in lst2:
        count = 0
        for x in lst1:
            if x == num:
                count += 1
        print(f"{num} : {count}")
if __name__ == "__main__":
    n = [5,3,2,2,1,5,5,7,5,10]
    m = [10,111,1,9,5,67,2]
    hashing_numbers(n,m)