class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        summ =  0
        for i in range(1,len(prices)):
            summ+=prices[i]-prices[i-1]
            summ = max(0,summ) #reset
            res = max(res,summ)
        return res
        



            

        

        