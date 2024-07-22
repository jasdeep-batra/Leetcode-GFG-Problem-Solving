class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        nww = 0
        res = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                curr += (prices[i]-prices[i-1])
            

        return curr





        

        