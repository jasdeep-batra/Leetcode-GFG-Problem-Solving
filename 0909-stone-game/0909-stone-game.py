class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #every time we have two options
        #for each option a recursive tree we can create and find if alice wins
        n = len(piles)
        def recursion(i,a,b,n):
            if i==n:
                return a>b
            ans = False
            if i%2==0:
                ans = recursion(i+1,a+piles[i],b,n) or recursion(i,a+piles[n-i-1],b,n-1)
            else:
                ans = recursion(i+1,a,b+piles[i],n) or recursion(i,a,b+piles[n-1-i],n-1)
            

            return ans
        return recursion(0,0,0,n)
        