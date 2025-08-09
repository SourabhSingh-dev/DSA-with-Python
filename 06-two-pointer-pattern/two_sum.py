"""
Link : https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1
        while (p2<len(nums)):
            if ((nums[p1] + nums[p2]) == target ):
                return [p1,p2]
            if (p2 == (len(nums) - 1)):
                p1 += 1
                p2 = p1 + 1
            else:
                p2 += 1

### Optimal Approach is using Hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for ind,num in enumerate(nums):
            comp = target - num
            if (comp in hash_dict):
                return [hash_dict[comp],ind]
            else:
                hash_dict[num] = ind