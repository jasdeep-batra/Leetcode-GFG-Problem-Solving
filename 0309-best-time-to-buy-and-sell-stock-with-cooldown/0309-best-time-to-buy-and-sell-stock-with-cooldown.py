class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def recursion(i, b):
            if i >= len(prices):
                return 0
            if (i,b) in memo:
                return memo[(i,b)]
            if b:
                profit = max(recursion(i+1, 0) - prices[i], recursion(i+1, 1))
                memo[(i,b)] = profit
            else:
                profit = max(prices[i] + recursion(i+2, 1), recursion(i+1, 0))
                memo[(i,b)] = profit
            return profit

        return recursion(0, 1)
