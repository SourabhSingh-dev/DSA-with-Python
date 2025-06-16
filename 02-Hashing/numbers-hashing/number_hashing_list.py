"""
Using the benefit of constraints
1 <= n[i] <= 10
"""
def hashing_list(lst1,lst2):
    hash_list = [0]*11 # 11 because of index 0 to 10(constraint)
    for num in lst1:
        hash_list[num] += 1
    for num in lst2:
        if num < 1 or num > 10:
            print(f"{num} : 0")
        else:
            print(f"{num} : {hash_list[num]}")
if __name__ == "__main__":
    n = [5,3,2,2,1,5,5,7,5,10]
    m = [10,111,1,9,5,67,2]
    hashing_list(n,m)