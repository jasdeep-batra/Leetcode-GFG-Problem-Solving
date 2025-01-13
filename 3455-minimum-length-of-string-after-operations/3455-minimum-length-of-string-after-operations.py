class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for key,value in freq.items():
            if (value >= 3):
                if (value%2==0):
                    ans+=2
                else:
                    ans+=1
            else:
                ans+=value
        return ans
            
        