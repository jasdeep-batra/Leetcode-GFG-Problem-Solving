class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(n+1)
        def helper(top):
            if top<0:
                return 0
            if top==0:
                return 1
            if top in memo:
                return memo[top]
            memo[top] = helper(top-1) + helper(top-2)
            return memo[top]

        return helper(n)
        