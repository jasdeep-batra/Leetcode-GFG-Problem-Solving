class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            # Check boundaries and if cell is water or already visited
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
                return
            # Mark as visited
            grid[i][j] = "2"
            # Recursively visit neighbors
            for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                bfs(i + x, j + y)
            return 
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans