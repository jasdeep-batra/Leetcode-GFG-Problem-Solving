class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[sys.maxsize]*n for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((i,j))
                    visit[i][j] = 0
        

        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        while queue:
            i,j = queue.popleft()
            for dx,dy in dirs:
                x,y = i+dx, j+dy
                if x>=0 and x<n and y>=0 and y<n:
                    if grid[x][y]==0 and visit[x][y] > (1 + visit[i][j]):
                        visit[x][y] = 1 + visit[i][j]
                        queue.append((x,y))

        print(visit)
        ans = 0
        for item in visit:
            ans = max(ans,max(item))
        return ans if ans!=sys.maxsize and ans!=0 else -1



            