class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        maxcherries = [0]
        @lru_cache(None)
        def recursion(i,j,k,l):
            #base condition
            if i>=m or j>=n or k>=m or l>=n or grid[i][j]==-1 or grid[k][l]==-1:                
                return -sys.maxsize      
            #base condition
            if i==m-1 and j==n-1 and k==m-1 and l==n-1:
                return grid[i][j]
            if i==k and j==l:
                cherry = grid[i][j]                        
            else:
                cherry = grid[i][j]+grid[k][l]
            
            ans1 = recursion(i+1,j,k+1,l)
            ans2 = recursion(i,j+1,k+1,l)
            ans3 = recursion(i+1,j,k,l+1)
            ans4 = recursion(i,j+1,k,l+1)
            cherry += max(ans1,ans2,ans3,ans4)
            return cherry

        return max(recursion(0,0,0,0),0)
        

