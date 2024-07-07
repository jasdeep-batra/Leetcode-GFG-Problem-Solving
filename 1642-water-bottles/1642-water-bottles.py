class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while((numBottles//numExchange)>0):    
            ans+=(numBottles//numExchange)
            empty = numBottles%numExchange

            numBottles = (numBottles//numExchange)+empty

        return ans;

        