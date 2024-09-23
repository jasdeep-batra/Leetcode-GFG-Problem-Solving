class Solution:
    def minExtraChar(self, s: str, dictt: List[str]) -> int:
        dictionary = set(dictt)
        n = len(s)
        dp = [0]*(n+1)

        for i in range(1,n+1):
            dp[i] = dp[i-1]+1

            for j in range(0,i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i],dp[j])

        return dp[n]

        