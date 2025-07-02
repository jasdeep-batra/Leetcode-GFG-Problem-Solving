class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #all direction open
        #by bfs might not work because you don't have any single point to start from...
        m,n = len(matrix),len(matrix[0])
        memo = {}
        def dfs(i,j,visit):
            print((i,j))
            if (i,j) in memo:
                return memo[(i,j)]
            visit.add((i,j))            
            step = 1
            maxdfs = 0
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                x,y = i+dx,j+dy
                # print(x,y)
                if x<0 or x>=m or y<0 or y>=n:
                    continue
                if matrix[x][y] > matrix[i][j]:
                    # print((x,y))
                    curr = dfs(x,y,visit)
                    maxdfs = max(maxdfs,curr)
                    step = 1 + maxdfs

            memo[(i,j)] = step
            return step
        ans = 0
        # visit = set()
        # print(dfs(2,0,visit))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visit = set()
                ans = max(ans,dfs(i,j,visit))

        print(memo)
        return ans
