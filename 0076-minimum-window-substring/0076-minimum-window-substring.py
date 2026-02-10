class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq = Counter(t)
        size = len(freq)
        ans = ""
        min_len = float('inf')
        i = 0
        for j in range(len(s)):
            if s[j] in freq:
                freq[s[j]]-=1
                if freq[s[j]]==0:
                    size-=1

            while size==0:
                if min_len > (j-i+1):
                    ans = s[i:j+1]
                    min_len = j-i+1
                    # print(ans)
                if s[i] in freq:
                    freq[s[i]]+=1
                    if freq[s[i]]>0:
                        size+=1
                i+=1

        return ans    
            