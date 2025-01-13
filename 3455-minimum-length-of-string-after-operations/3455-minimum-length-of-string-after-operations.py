class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0]*26
        ans = 0
        for char in s:
            freq[ord(char)-ord('a')]+=1
        for num in freq:
            if num >=3:
                if num%2==0:
                    ans+=2
                else:
                    ans+=1
            else:
                ans+=num
                
        return ans
            
        