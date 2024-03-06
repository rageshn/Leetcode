"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 
Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)

        found = {}
        result = []
        for i in nums:
            found[i] = True
        
        for i in range(1, l+1):
            if i not in found:
                result.append(i)
        
        return result
    

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        result = []
        for i in range(1,l+1):
            if nums[i-1] > 0:
                result.append(i)
        
        return result