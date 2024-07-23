class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize for i in range(n+1)]
        dp[0] = 0
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]+j >= i:
                    dp[i] = min(dp[j]+1,dp[i])
        return dp[n-1]

            



        