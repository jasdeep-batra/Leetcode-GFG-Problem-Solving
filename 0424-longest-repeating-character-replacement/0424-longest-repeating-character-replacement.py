class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictt = Counter()
        max_freq = 0
        i,j =0,0
        ans = 0
        while j<len(s):
            dictt[s[j]]+=1
            max_freq = max(max_freq,dictt[s[j]])

            while ((j-i+1) - max_freq) > k:
                dictt[s[i]]-=1
                i+=1
            
            ans = max(ans,j-i+1)
            j+=1
                

        return ans