"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""
def moveZeroes(num):
    i = 0
    n = len(num)
    for j in range(1,n):
        if num[i] == 0 and num[j] != num[i]:
            num[i],num[j] = num[j],num[i]
            i += 1
        if num[i] != 0:
            i += 1
arr = nums = [0, 1, 0, 0, 2, 3]
# arr = [0,1,0,3,12]
moveZeroes(arr)
print(arr)