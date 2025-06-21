"""
Using dictionary instead of List, list wont be useful if we dont have this constraint
1<= n[i] <= 10
"""
def hashing_dict(lst1,lst2):
    hash_dict = dict()
    for num in lst1:
        hash_dict[num] = hash_dict.get(num,0)+1
    for num in lst2:
        if num in hash_dict:
            print(f"{num} : {hash_dict[num]}")
        else:
            print(f"{num} : 0")
if __name__ == "__main__":
    n = [5,3,2,2,1,5,5,7,5,10]
    m = [10,111,1,9,5,67,2]
    hashing_dict(n,m)