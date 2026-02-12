class Solution:
    def balancedString(self, s: str) -> int:
        count =  Counter(s)
        k = (len(s))//4
        i = 0
        ans = float('inf')
        if all(count[c] == k for c in "QWER"):
            return 0

        for j in range(len(s)):
            count[s[j]]-=1
            while max(count.values()) <=k:
                ans = min(ans,j-i+1) 
                count[s[i]]+=1
                i+=1

        return ans