class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        #no need of dijikstra
        row,col = len(grid),len(grid[0])
        visit = [[sys.maxsize]*col for _ in range(row)]
        visit[0][0] = 0
        visited = set()
        queue = deque()
        queue.append((0,0,0))
        dirs = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}

        while queue:
            i,j,cost = queue.popleft()
            for key,values in dirs.items():
                dx,dy = values
                x,y = i+dx,j+dy
                if 0<=x<row and 0<=y<col:
                    new_cost = 0 if grid[i][j]==key else 1
                    if visit[x][y] > (new_cost + visit[i][j]):
                        queue.append((x,y,new_cost)) #we might not be properly storing state
                        visit[x][y] = new_cost + visit[i][j]
                        visited.add((x,y,new_cost))

        for item in visit:
            print(item)
        return visit[row-1][col-1]
                # if grid[i][j]==key:




        