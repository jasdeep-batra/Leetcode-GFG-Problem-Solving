class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        dp[0] = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            ans = max(ans,prices[i]-dp[i-1])
            # print(prices[i]-dp[i-1])
            dp[i] = min(prices[i],dp[i-1])

        print(dp)
        return ans

