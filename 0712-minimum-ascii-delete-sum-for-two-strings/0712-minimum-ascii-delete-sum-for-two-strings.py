class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        def helper(i,j):
            if i>=len(s1):
                dell = 0
                while j<len(s2):
                    dell+=ord(s2[j])
                    j+=1
                return dell
            if j>=len(s2):
                dell = 0
                while i<len(s1):
                    dell+=ord(s1[i])
                    i+=1
                return dell
            if (i,j) in memo:
                return memo[(i,j)]
            ans = float('inf')
            if s1[i]==s2[j]:
                ans = min(ans,helper(i+1,j+1))
            else:
                ans = min(ord(s1[i])+helper(i+1,j),ord(s2[j])+helper(i,j+1))
            memo[(i,j)] = ans
            return ans

        return helper(0,0)
