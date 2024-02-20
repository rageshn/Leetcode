class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        sums = []
        for i in range(l):
            if i == 0:
                sums.append(nums[i])
            else:
                s = 0
                r = nums[:i+1]
                for v in r:
                    s += v
                sums.append(s)
        
        return sums