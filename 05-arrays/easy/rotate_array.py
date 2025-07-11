"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""
# def right_rotate(nums,k):
#     n = len(nums)
#     if k == 0:
#         return
#     temp = nums[n-1]
#     for i in range(n-2,-1,-1):
#         nums[i+1] = nums[i]
#     nums[0] = temp
#     right_rotate(nums,k-1)

## TLE Error  

def right_rotate(arr,k):
    n = len(arr)
    if k > n:
        k = k % n
    i = 0
    j = n - 1
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    i = 0
    j = k-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    i = k
    j = n - 1 
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
if __name__ == "__main__":
    sample_input = [1,2,3,4,5,6,7]
    right_rotate(sample_input,k=3)
    print(sample_input)