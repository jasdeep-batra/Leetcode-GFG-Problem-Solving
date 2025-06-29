class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)  # ✅ Convert list to set for O(1) lookup
        n = len(s)
        dp = [[0]*(n) for _ in range(n)]
        
        for i in range(n):
            if s[i] in wordDict:
                dp[i][i] = 1
        

        
        for i in range(1,n):
            for j in range(0,n-i):
                if s[j:j+i+1] in wordDict:
                    dp[j][i+j] = 1
                else:
                    k = j
                    while k < (i+j):
                        if (dp[j][k] and dp[k+1][j+i]):
                            dp[j][i+j] = 1
                            break   # ✅ Early exit on finding valid split
                        k+=1

        for item in dp:
            print(item)

        return True if dp[0][n-1] else False
