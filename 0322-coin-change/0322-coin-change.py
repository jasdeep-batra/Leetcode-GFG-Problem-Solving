class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')]*(amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = float('inf')
        for i in range(1,len(coins)+1):
            dp[i][0] = 0
        
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]],dp[i-1][j])
        return dp[len(coins)][amount] if dp[len(coins)][amount]!=float('inf') else -1


        