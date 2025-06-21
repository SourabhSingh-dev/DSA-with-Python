"""
Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

Link : https://www.geeksforgeeks.org/problems/find-the-frequency/1 

Examples :

Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5
Explanation: Frequency of 1 is 5.
Input: arr = [1, 2, 3, 3, 2, 1], x=2
Output: 2
Explanation: Frequency of 2 is 2.
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105
1 <= x <= 105


"""
def findFrequency(arr, x):
    hash_dict = dict()
    for element in arr:
        hash_dict[element] = hash_dict.get(x,0)+1
    # if x in arr:
    #     return hash_dict[x]
    # else:
    #     return 0
    return hash_dict.get(x,0)
if __name__ == "__main__":
    sample_arr = [1,2,3,3,2,1]
    x = 21
    print("Output : ",findFrequency(sample_arr,x))