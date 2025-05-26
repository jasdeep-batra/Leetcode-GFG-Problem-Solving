class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        ans = [[float('inf')]*n for _ in range(m)]
        dirs = ((-1,0),(1,0),(0,-1),(0,1))
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    ans[i][j]=0
                    queue.append((i,j))

        while queue:
            i,j = queue.popleft()
            for dx,dy in dirs:
                x,y = i+dx,j+dy
                if x>=0 and x<m and y>=0 and y<n:
                    if ans[x][y] > 1+ans[i][j]:
                        ans[x][y] = 1 + ans[i][j]
                        queue.append((x,y))

        return ans




        