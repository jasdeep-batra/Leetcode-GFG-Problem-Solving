class Solution:
    def maxScore(self, s: str) -> int:
        # zero on left and one on right
        #formula since it is binary
        ans = 0
        for i in range(len(s)-1):
            ans = max(ans,s[0:i+1].count('0')+s[i+1:len(s)+1].count('1'))

        return ans

        