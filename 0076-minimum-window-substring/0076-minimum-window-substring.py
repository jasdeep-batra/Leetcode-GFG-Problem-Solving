class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for char in t:
            freq[char]+=1
        
        i,j = 0,0
        ans = float('inf')
        res = ""
        count = len(t)
        while j < len(s):
            if s[j] in freq:
                freq[s[j]]-=1
                if freq[s[j]] >= 0:
                    count-=1
            
            while count<=0:
                if (j - i + 1) < ans:
                    ans = j - i + 1
                    res = s[i:j+1]
                
                if s[i] in freq:
                    freq[s[i]]+=1
                    if freq[s[i]]>0:
                        count+=1 
                i+=1

            j+=1

        return res
