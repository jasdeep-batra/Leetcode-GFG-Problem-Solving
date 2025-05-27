class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        visit = [[sys.maxsize]*n for _ in range(n)]
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        def changeId(i,j):
            grid[i][j] = 2
            visit[i][j] = 0
            queue.append((i,j))
            # print(i,j,"yo")
            for dx,dy in dirs:
                x,y=i+dx,j+dy
                if x>=0 and x<n and y>=0 and y<n:
                    if grid[x][y]==1:
                        # print("no",x,y)
                        changeId(x,y)
            return 
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    changeId(i,j)
                    found=True
                    break
            if found:
                break
        # for item in visit:
        #     print(item)
        # print(queue)
        ans = sys.maxsize
        while queue:
            i,j = queue.popleft()
            for dx,dy in dirs:
                x,y = i+dx,j+dy
                if x>=0 and x<n and y>=0 and y<n:
                    if grid[x][y]==1:
                        ans = min(ans,visit[i][j])
                        continue
                    elif grid[x][y]==0 and visit[x][y] > (1 + visit[i][j]):
                        visit[x][y] = 1 + visit[i][j]
                        queue.append((x,y))
            # print(queue)
        # for item in visit:
        #     print(item)
        return ans
                    
