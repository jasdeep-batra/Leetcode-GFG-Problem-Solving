class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [0]*len(prices)
        # dp[0] = prices[0]
        ans = 0
        price = 0
        for i in range(1,len(prices)):
            price+= prices[i]-prices[i-1]
            price = max(price,0)
            ans = max(ans,price)
        return ans

