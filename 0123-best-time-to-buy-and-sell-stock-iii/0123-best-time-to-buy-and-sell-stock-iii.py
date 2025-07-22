class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find diff condition
        memo = {}
        @lru_cache(None)
        def recursion(i,buy,count):
            if i>=len(prices):
                return 0
            if count==0:
                return 0
            profit= 0
            if buy==1:
                return max(-prices[i] + recursion(i+1,0,count), recursion(i+1,1,count))
            else:
                return max(prices[i] + recursion(i+1,1,count-1),recursion(i+1,0,count))

            return profit
        return recursion(0,1,2)