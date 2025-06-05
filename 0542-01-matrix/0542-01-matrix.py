class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        visit = [[float('inf')]*col for _ in range(row)]
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    queue.append((i,j))
                    visit[i][j] = 0
        #start BFS
        step = 1
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    x,y = i+dx,j+dy
                    if 0<=x<row and 0<=y<col:
                        if visit[x][y] > 1+visit[i][j]:
                            visit[x][y] = visit[i][j]+1
                            queue.append((x,y))
        return visit


        