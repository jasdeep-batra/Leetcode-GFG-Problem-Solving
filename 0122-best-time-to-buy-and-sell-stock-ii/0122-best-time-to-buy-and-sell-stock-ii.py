class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for i in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            dp[i][0] = max(prices[i]+dp[i+1][1],dp[i+1][0])
            dp[i][1] = max(-prices[i]+dp[i+1][0],dp[i+1][1])

        return dp[0][1]