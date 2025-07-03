class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        maxcherries = [0]
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(m)]
        def recursion(i,j,k):
            #base condition
            l = i+j-k
            if i>=m or j>=n or k>=m or l>=n or grid[i][j]==-1 or grid[k][l]==-1:                
                return -sys.maxsize      
            #base condition
            if dp[i][j][k]!=None:
                return dp[i][j][k]
            if i==m-1 and j==n-1 and k==m-1 and l==n-1:
                return grid[i][j]
            if i==k and j==l:
                cherry = grid[i][j]                        
            else:
                cherry = grid[i][j]+grid[k][l]
            
            ans1 = recursion(i+1,j,k+1)
            ans2 = recursion(i,j+1,k+1)
            ans3 = recursion(i+1,j,k)
            ans4 = recursion(i,j+1,k)
            cherry += max(ans1,ans2,ans3,ans4)
            dp[i][j][k] = cherry
            return cherry
        
        return max(recursion(0,0,0),0)
        

