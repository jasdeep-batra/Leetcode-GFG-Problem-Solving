class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        #base case which I could think of is : if out of boundindex then retunrn 1
        #stopping condition at maxMoves
        mat = [[0 for i in range(n)]for i in range(m)]
        MOD = 10**9+7
        dp =  {}
        def recursion(i,j,moves):
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            if moves==0:
                return 0
            if (i,j,moves) in dp:
                return dp[(i,j,moves)]
            path = recursion(i+1,j,moves-1)+recursion(i,j+1,moves-1)+recursion(i-1,j,moves-1)+recursion(i,j-1,moves-1)
            dp[(i,j,moves)] = path%MOD
            
            return path%MOD
            
        return recursion(startRow,startColumn,maxMove)%MOD
