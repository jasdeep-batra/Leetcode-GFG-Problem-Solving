class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        target_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    target_count+=1
        time = 0
        while queue and target_count:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    x,y = i+dx,j+dy
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
                        queue.append((x,y))
                        target_count-=1
                        grid[x][y]=2
            time+=1
        return time if target_count==0 else -1

