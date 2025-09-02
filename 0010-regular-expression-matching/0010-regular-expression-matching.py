class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def helper(i,j):
            #base condition
            if j>=len(p):
                return i==len(s)
            
            curr_char = i<len(s) and (s[i]==p[j] or p[j]=='.')

            if j+1<len(p) and p[j+1]=='*':
                return helper(i,j+2) or (curr_char and helper(i+1,j))
            else:
                return curr_char and helper(i+1,j+1)
        return helper(0,0)



        