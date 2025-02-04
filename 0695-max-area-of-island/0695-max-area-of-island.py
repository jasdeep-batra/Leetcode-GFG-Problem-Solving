class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def isValid(a,b):
            if a>=0 and b>=0 and a<len(grid) and b<len(grid[0]):
                return True
            return False
        def bfs(i,j):
            queue = [(i,j)]
            grid[i][j] = 0
            res = 0
            while len(queue)!=0:
                ii,jj = queue.pop(0)
                res += 1
                for x,y in dirs:
                    dx,dy = ii+x,jj+y
                    if isValid(dx,dy) and (grid[dx][dy]==1):
                        queue.append((dx,dy))
                        grid[dx][dy]=0

            
            return res
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans = max(ans,bfs(i,j))

        return ans
        # [1,1,0,0,0],
        # [1,1,0,0,0],
        # [0,0,0,1,1]
        # [0,0,0,1,1]