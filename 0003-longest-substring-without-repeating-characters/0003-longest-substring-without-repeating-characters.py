class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictt = {}
        if not s:
            return 0
        left,ans = -1,0
        for i in range(len(s)):
            if s[i] in dictt and dictt[s[i]] > left:
                left = dictt[s[i]]
            dictt[s[i]] = i
            ans = max(ans,i-left)

        
        return ans

