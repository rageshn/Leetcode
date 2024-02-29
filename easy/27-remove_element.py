"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
-------------
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def removeElement(nums, val):
    front_index = 0
    last_replace_index = len(nums) - 1
    while front_index <= last_replace_index:
        if nums[front_index] == val:
            if nums[last_replace_index] != val:
                temp = nums[front_index]
                nums[front_index] = nums[last_replace_index]
                nums[last_replace_index] = temp
                del nums[last_replace_index]
                last_replace_index -= 1
            else:
                del nums[last_replace_index]
                last_replace_index -= 1
        else:
            front_index += 1


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_to_shift = len(nums) - 1
        i = 0

        while i <= index_to_shift:
            if nums[i] == val:
                if nums[index_to_shift] == val:
                    #del nums[index_to_shift]
                    nums.pop(index_to_shift)
                    index_to_shift -= 1
                else:
                    nums[i] = nums[index_to_shift]
                    #del nums[index_to_shift]
                    nums.pop(index_to_shift)
                    index_to_shift -= 1
            else:
                i += 1


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0

        while i <= j:
            if nums[i] == val and nums[j] == val:
                j -= 1
            elif nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] != val and nums[j] == val:
                j -= 1
            elif nums[i] != val and nums[j] != val:
                i += 1
        return i