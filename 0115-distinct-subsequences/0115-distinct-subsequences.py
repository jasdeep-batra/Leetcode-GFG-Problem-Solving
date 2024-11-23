class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {(-1,-1):0}
        def helper(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            if j == len(t):
                return 1  # Found an answer
            if i == len(s):
                return 0  # Exhausted s without matching t

            # Initialize ans locally
            ans = 0
            if s[i] == t[j]:
                ans += helper(i + 1, j + 1)  # Match and move both pointers
            ans += helper(i + 1, j)  # Skip current character in s
            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return helper(0, 0)

# class Solution:
#     def numDistinct(self,s,t):



        