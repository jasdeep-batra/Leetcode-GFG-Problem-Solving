class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        summ = 0
        i = 0
        ans = 0
        for j in range(len(s)):
            summ+=abs(ord(s[j])-ord(t[j]))
            while i<=j and summ > maxCost:
                summ-=abs(ord(s[i])- ord(t[i]))
                i+=1

            ans = max(j-i+1,ans)


        return ans
