class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,2
        if n<=1:
            return a if n==1 else 0
        for i in range(3,n+1):
            temp = b
            b = a+b
            a = temp

        return b
        
        