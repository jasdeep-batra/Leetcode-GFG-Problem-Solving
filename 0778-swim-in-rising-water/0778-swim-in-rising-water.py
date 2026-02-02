class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = n = len(grid)
        pq = [(grid[0][0],0,0)]
        ans = sys.maxsize
        visit = [[False]*n for _ in range(n)]
        visit[0][0]=True
        while pq:
            time,i,j = heapq.heappop(pq)
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                x,y = i+dx,j+dy
                if x>=0 and x<m and y>=0 and y<n and not visit[x][y]:
                    visit[x][y] = True
                    #perform action
                    if x==n-1 and y==n-1:
                        ans = min(ans,max(grid[x][y],time))
                    heapq.heappush(pq,(max(grid[x][y],time),x,y))
        return ans if ans!=sys.maxsize else 0