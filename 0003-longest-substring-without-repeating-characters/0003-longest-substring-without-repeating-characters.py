class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = {}
        ans = float('-inf')
        i=0
        for j in range(len(s)):
            if s[j] not in mapp:
                mapp[s[j]] = j

            else:
                ans = max(ans,j-i)
                if mapp[s[j]] >= i:
                    i = mapp[s[j]]+1
                mapp[s[j]] = j
        
        if ans==float('-inf'):
            ans = len(s)
        else:
            ans = max(ans,len(s)-i)


        return ans
