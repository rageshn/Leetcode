class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for cust in accounts:
            wealth = 0
            for v in cust:
                wealth += v
            
            if wealth > max_wealth:
                max_wealth = wealth
            
        return max_wealth