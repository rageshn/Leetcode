class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for v in nums:
            result.append(v * v)
        
        result.sort()
        return result