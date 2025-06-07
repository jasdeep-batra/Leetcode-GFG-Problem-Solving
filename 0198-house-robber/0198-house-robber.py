class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rec(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            #two options
            money = max(nums[i]+rec(i+2),rec(i+1))
            memo[i] = money
            return money
        
        ans = rec(0)
        return ans
            
        