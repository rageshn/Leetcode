"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Input: nums = [1,0,1,1,0,1]
Output: 2
"""


def findMaxConsecutiveOnes(nums):
    max_val = 0
    curr_max = 0
    for number in nums:
        if number == 1:
            curr_max += 1
        else:
            if curr_max > max_val:
                max_val = curr_max
            curr_max = 0
    if curr_max > max_val:
        max_val = curr_max
    return max_val

