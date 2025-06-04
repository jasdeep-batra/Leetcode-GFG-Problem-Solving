class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        #state based bfs
        heap = []
        heapq.heappush(heap,(0,0,0))
        dirs = ((0,1),(0,-1),(1,0),(-1,0)) #i,j,obstacles
        tx,ty = len(grid),len(grid[0])
        visit = [[sys.maxsize]*(ty+1) for _ in range(tx+1)]
        visit[0][0] = 0
        while heap:
            obs,i,j = heapq.heappop(heap)
            if i==tx-1 and j==ty-1:
                return obs
            
            for dx,dy in dirs:
                x,y = i+dx,j+dy
                if 0<=x<tx and 0<=y<ty:
                    if visit[x][y] > obs + grid[x][y]:
                        new_obs = obs + grid[x][y]
                        heapq.heappush(heap,(new_obs,x,y))
                        visit[x][y] = new_obs
        return -1


        