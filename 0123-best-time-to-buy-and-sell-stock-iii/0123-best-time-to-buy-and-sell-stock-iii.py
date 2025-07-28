class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def recursion(i,buy,k):
            if i==len(prices) or k==0:
                return 0
            profit = 0
            if buy==1:
                profit = max(-prices[i] + recursion(i+1,0,k),recursion(i+1,1,k))
            else:
                profit = max(prices[i]+recursion(i+1,1,k-1),recursion(i+1,0,k))
            return profit
        return recursion(0,1,2)