class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = {}
        
        def helper(i, j):
            # Check if this subproblem has already been solved
            if (i, j) in dp:
                return dp[(i, j)]
            
            # Base cases
            if i == len(s1):
                # Sum ASCII values for remaining characters in s2
                return sum(ord(s2[k]) for k in range(j, len(s2)))
            if j == len(s2):
                # Sum ASCII values for remaining characters in s1
                return sum(ord(s1[k]) for k in range(i, len(s1)))
            
            # If characters match, move both pointers forward
            if s1[i] == s2[j]:
                dp[(i, j)] = helper(i + 1, j + 1)
            else:
                # Two possibilities: delete from s1 or delete from s2
                delete_s1 = ord(s1[i]) + helper(i + 1, j)
                delete_s2 = ord(s2[j]) + helper(i, j + 1)
                dp[(i, j)] = min(delete_s1, delete_s2)
            
            return dp[(i, j)]
        
        return helper(0, 0)
