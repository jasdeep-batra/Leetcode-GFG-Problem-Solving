class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        summ = sum(stones)//2

        dp = [[False]*(summ+1) for i in range(n+1)]
        for i in range(0,n+1):
            dp[i][0] = True
        
        for i in range(1,n+1):
            for j in range(1,summ+1):
                if j >= stones[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - stones[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        ans = 0
        for i in range(summ,-1,-1):
            if dp[n][i]==True:
                ans = i
                break
        return sum(stones) - 2*(ans)
            



            

