"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [0] * l
        prd = 1
        zero_count  = 0
        for i in nums:
            if i != 0:
                prd = prd * i
            else:
                zero_count += 1

        if zero_count > 1:
            return output
        elif zero_count == 1:
            for i in range(l):
                if nums[i] == 0:
                    output[i] = prd
                else:
                    output[i] = 0
            return output
        else:
            for i in range(l):
                output[i] = prd // nums[i]
            return output