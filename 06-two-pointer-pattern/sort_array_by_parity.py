"""

Link : https://leetcode.com/problems/sort-array-by-parity/description/

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
# First version — simple list building (O(n) time, O(n) space)

python
Copy
Edit
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        nums1 = []
        nums2 = []
        res = []
        for i in nums:
            if i % 2 == 0:
                nums1.append(i)
            else:
                nums2.append(i)
        res = nums1 + nums2
        return res
# Second version — two pointers but many branches (O(n) time, O(1) space)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        p1 = 0
        p2 = 1
        for i in range(0, len(nums)):
            if (p1 == len(nums) or (p2 == len(nums))):
                break
            elif ((nums[p1] % 2 != 0) and (nums[p2] % 2 == 0)):
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
            elif ((nums[p1] % 2 == 0) and (nums[p2] % 2 == 0)):
                p1 += 1
                p2 += 1
            elif ((nums[p1] % 2 == 0) and (nums[p2] % 2 != 0)):
                p1 += 1
                p2 += 1
            elif ((nums[p1] % 2 != 0) and (nums[p2] % 2 != 0)):
                p2 += 1
        return nums

# Third version — two pointers 

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            if ((nums[p1] % 2 != 0) and (nums[p2] % 2 == 0)):
                nums[p1], nums[p2] = nums[p2], nums[p1]
            if nums[p1] % 2 == 0:
                p1 += 1
            if nums[p2] % 2 != 0:
                p2 -= 1
        return nums