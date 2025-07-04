"""
You are given an array arr[] containing positive integers. The elements in the array arr[] range from 1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your task is to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

Link : https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

Examples

Input: arr[] = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.
Input: arr[] = [3, 3, 3, 3]
Output: [0, 0, 4, 0]
Explanation: We have: 1 occurring 0 times, 2 occurring 0 times, 3 occurring 4 times, and 4 occurring 0 times.
Input: arr[] = [1]
Output: [1]
Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()
"""
def frequencyCount(arr):
    # hash_dict = dict()
    result = [0]*len(arr)
    # for element in arr:
    #     hash_dict[element] = hash_dict.get(element,0)+1
    # for keys,values in hash_dict.items():
    #     result[keys-1] = values
    # return result
    for element in arr:
        result[element - 1] += 1
    return result
if __name__ == "__main__":
    sample_arr = [1]
    print("Output : ",frequencyCount(sample_arr))