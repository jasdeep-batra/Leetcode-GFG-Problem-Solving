class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[0,0,0] for _ in range(len(prices))]
        # [buy,sell,hold]
        # in dp we will be storing profit so each day even if buy then profit will be negative
        dp[0][0] = -prices[0]        
        for i in range(1,len(prices)):
            dp[i][2] = max(dp[i-1][1],dp[i-1][2]) #rest
            dp[i][0] = max(dp[i-1][2]-prices[i],dp[i-1][0]) #buy or hold
            dp[i][1] = prices[i]+dp[i-1][0]#sell
        
        return max(dp[len(prices)-1][1] , dp[len(prices)-1][2])