class Solution:
    def maxProfit(self,k:int, prices: List[int]) -> int:        
        if k > len(prices)//2:
            profit = 0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:                    
                    profit+=(prices[i]-prices[i-1])

            return profit
        dp = [[0,float(-inf)] for i in range(k+1)]
        
        for price in prices:
            for i in range(1,k+1):
                dp[i][0] = max(dp[i][0],dp[i][1]+price)
                dp[i][1] = max(dp[i][1],dp[i-1][0]-price)

        return dp[k][0]