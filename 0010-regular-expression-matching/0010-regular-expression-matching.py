class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #base condition
        @lru_cache(None)
        def helper(i,j):
            if j==len(p):
                return i>=len(s)

            if i<len(s):
                firstchar = s[i]==p[j] or p[j]=='.'
            if j+1<len(p)  and p[j+1]=='*':
                ans = helper(i,j+2) or helper(i+1,j)
            else:
                ans = firstchar and helper(i+1,j+1)
            return ans
        return helper(0,0)