class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # is it a problem of sliding window
        # or is it a problem of map
        j = 0
        vow = {0:-1}
        mask = 0  #00000
        ans = 0
        #if mask is 0 that means all the vowels are even or 0
        while j < len(s):
            if s[j]=='a':
                mask ^= (1<<0)
            elif s[j]=='e':
                mask^=(1<<1)
            elif s[j]=='i':
                mask^=(1<<2)
            elif s[j]=='o':
                mask^=(1<<3)
            elif s[j]=='u':
                mask^= (1<<4)
            if mask in vow:
                ans = max(ans,j-vow[mask])
            else:
                vow[mask] =j
            j+=1
        return ans
            
            
            
        