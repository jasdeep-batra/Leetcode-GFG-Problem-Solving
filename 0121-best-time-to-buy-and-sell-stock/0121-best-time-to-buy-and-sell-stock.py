class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        summ = 0 
        res = 0
        for i in range(1,len(prices)):
            summ += (prices[i]-prices[i-1])
            summ = max(summ,0)
            res  = max(summ,res)
        return res

        