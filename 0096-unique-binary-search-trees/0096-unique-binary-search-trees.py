class Solution:
    def numTrees(self, n: int) -> int:
        # start left from -1
        self.dp = {}
        def helper(n):
            if n==1 or n==0:
                return 1
            if n==2:
                return 2
            ans = 0
            if n in self.dp:
                return self.dp[n]
            for i in range(1,n+1):
                ans += helper(i-1)*helper(n-i)
            self.dp[n] = ans
            return ans
        return helper(n)



            