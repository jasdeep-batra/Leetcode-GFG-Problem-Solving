class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for _ in range(len(text1))]
        def helper(i,j):
            #base condition
            if i>=len(text1) or j>=len(text2):
                return 0
            count = 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if text1[i]==text2[j]:
                count = 1 + helper(i+1,j+1)
            else:
                count = max(helper(i+1,j),helper(i,j+1))
            memo[i][j] = count
            return count
        return helper(0,0)