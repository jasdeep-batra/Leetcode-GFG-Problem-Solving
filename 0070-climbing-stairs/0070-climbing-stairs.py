class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def rec(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if n in memo:
                return memo[n]
            step = rec(n-1)
            step+=rec(n-2)
            memo[n] = step
            return step
        return rec(n)
        