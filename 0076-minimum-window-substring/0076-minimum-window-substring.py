class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for char in t:
            freq[char]+=1
        
        i,j = 0,0
        ans = float('inf')
        res = ""
        def get_sum_of_freq():
            return sum([val for char, val in freq.items() if val > 0])
        while j < len(s):
            if s[j] in freq:
                freq[s[j]]-=1
            
            while get_sum_of_freq()==0:
                if (j - i + 1) < ans:
                    ans = j - i + 1
                    res = s[i:j+1]
                
                if s[i] in freq:
                    freq[s[i]]+=1
                i+=1

            j+=1

        return res
