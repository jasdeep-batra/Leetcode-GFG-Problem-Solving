class Solution:
    def maxProfit(self,k:int, prices: List[int]) -> int:        
        memo = [[[-1]*2 for _ in range(k+1)] for i in range(len(prices)+1)]
        def recursion(i,buy,k):
            if i==len(prices) or k==0:
                return 0
            if memo[i][k][buy]!=-1:
                return memo[i][k][buy]
            profit = 0
            if buy==1:
                profit = max(-prices[i] + recursion(i+1,0,k),recursion(i+1,1,k))
                memo[i][k][buy] = profit
            else:
                profit = max(prices[i]+recursion(i+1,1,k-1),recursion(i+1,0,k))
                memo[i][k][buy] = profit
            return profit
        return recursion(0,1,k)