class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at every step we have two options either buy or sell there if you sell then buy at next or if you buy then sell at next r somewhere
        #should we use recursion
        profit = [0]*(len(prices)+1)
        mini = [0]*(len(prices)+1)
        mini[0] = prices[0]
        #could be a reverse dp
        for i in range(1,len(prices)):
            # mini[i] = min(mini[i-1],prices[i])
            profit[i] = max(profit[i],profit[i-1]+prices[i]-prices[i-1],profit[i-1])

        return max(profit)



