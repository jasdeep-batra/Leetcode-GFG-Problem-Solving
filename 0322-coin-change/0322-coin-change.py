class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #here you  can repeat the coin pick again
        memo = {}
        def helper(i,amt):
            if i>=len(coins) or amt<0:
                return sys.maxsize
            if amt==0:
                return 0
            if (i,amt) in memo:
                return memo[(i,amt)]
            # print("stack: ",i," : ",amt-coins[i])
            step = 1 + helper(i,amt-coins[i])
            # print("step:", step)
            step = min(step,helper(i+1,amt))
            memo[(i,amt)] = step
            return step


        ans = helper(0,amount)
        return helper(0,amount) if ans!=sys.maxsize else -1



            

