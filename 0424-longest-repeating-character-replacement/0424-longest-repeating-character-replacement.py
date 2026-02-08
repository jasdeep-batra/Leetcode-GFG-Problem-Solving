class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #global vs local problem here we dont have a fix char which has max freq so it can change wqith window
        #there form no fixed char
        count  = {}

        i,j = 0,0
        max_freq = 0
        ans = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j],0)+1
            max_freq = max(max_freq,count[s[j]])

            while (j-i+1) - max_freq > k:
                count[s[i]]-=1
                i+=1

            ans = max(ans,j-i+1)

        return ans
