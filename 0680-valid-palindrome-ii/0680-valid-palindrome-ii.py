class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)<3:
            return True
        i,j = 0,len(s)-1

        while j>i:
            if s[i]!=s[j]:
                dx,dy = i+1,j
                while dx<dy and s[dx]==s[dy]:
                    dx+=1
                    dy-=1

                ans = dx>=dy
                dx,dy = i,j-1
                while dx<dy and s[dx]==s[dy]:
                    dx+=1
                    dy-=1

                ans = ans or (dx>=dy)
                return ans
            i+=1
            j-=1
        return True